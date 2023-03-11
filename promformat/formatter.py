import functools
from contextlib import contextmanager
from typing import Optional

from antlr4 import ErrorNode, TerminalNode, CommonTokenStream, ParserRuleContext
from antlr4.Token import CommonToken

from promformat.ast_nodes import (
    Number,
    MultOpNode,
    String,
    FunctionNode,
    LabelNode,
    InstantSelectorNode,
    MatrixSelectorNode,
    AggregationNode,
    LabelNameNode,
    SubqueryRangeNode,
    SubqueryNode,
    MetricNameNode,
    CompareOperationNode,
    AndUnlessOperationNode,
    OrOperationNode,
    UnaryOpNode,
    AddOpNode,
    Grouping,
    PowOpNode,
    ParensNode,
    OnIgnoring,
    GroupLeftRight,
    OffsetNode,
    LabelList,
    Parameter,
    ParameterListNode,
    ByWithoutNode,
)
from promformat.buffer import SmartBuffer
from promformat.error import UnEqualParseTreeError
from promformat.parser.PromQLParser import PromQLParser
from promformat.parser.PromQLParserVisitor import PromQLParserVisitor

SENTINEL = object()


class ParseTreeValidator:
    def validate(self, left, right):
        if type(left) != type(right):
            raise UnEqualParseTreeError(
                f"Expected: {type(left).__name__}, found: {type(right).__name__}"
            )
        elif left.getText() != right.getText():
            raise UnEqualParseTreeError(
                f"Expected:\n{left.getText()}\nFound:\n{right.getText()}\n"
            )
        if isinstance(left, (ErrorNode, TerminalNode)):
            return
        left_children, right_children = left.getChildren(), right.getChildren()
        for left, right in zip(left_children, right_children):
            if type(left) != type(right):
                raise UnEqualParseTreeError(
                    f"Expected: {type(left).__name__}, found: {type(right).__name__} on child"
                )
            self.validate(left, right)

        left_empty, right_empty = (
            next(left_children, SENTINEL) == SENTINEL,
            next(right_children, SENTINEL) == SENTINEL,
        )
        if not left_empty:
            raise UnEqualParseTreeError(
                f"Node: {type(left).__name__} has extra children"
            )
        if not right_empty:
            raise UnEqualParseTreeError(
                f"Node: {type(right).__name__} has extra children"
            )


class BuildAstVisitor(PromQLParserVisitor):
    def __init__(self):
        self.prev_index = 0

    def visit(self, ctx):
        result = super().visit(ctx)
        if ctx.start.tokenIndex != self.prev_index:
            comment_tokens = self._extract_comments_from_context(ctx)
            if comment_tokens:
                result.comments = comment_tokens
                self.prev_index = ctx.start.tokenIndex
        return result

    def visitExpression(self, ctx: PromQLParser.ExpressionContext):
        return self.visit(ctx.vectorOperation())

    def visitVectorOperation(self, ctx: PromQLParser.VectorOperationContext):
        if ctx.powOp():
            left, right = self._extract_left_right_vector_operations(ctx)
            op = ctx.powOp().POW().getText()
            grouping = self._extract_grouping(grouping=ctx.powOp().grouping())
            return PowOpNode(
                ctx,
                left=left,
                right=right,
                operator=op,
                grouping=grouping,
            )
        elif ctx.addOp():
            left, right = self._extract_left_right_vector_operations(ctx)
            op_codes = ("ADD", "SUB")
            context = ctx.addOp()
            op = self._extract_op(context, op_codes)
            grouping = self._extract_grouping(grouping=context.grouping())
            return AddOpNode(
                ctx,
                left=left,
                right=right,
                operator=op.getText(),
                grouping=grouping,
                comments=self._extract_comments_from_context(context),
            )
        elif ctx.unaryOp():
            vector = ctx.vectorOperation()
            assert len(vector) == 1
            operand = self.visit(vector[0])
            context = ctx.unaryOp()
            op_codes = ("ADD", "SUB")
            op = self._extract_op(context, op_codes)
            return UnaryOpNode(
                ctx,
                operator=op.getText(),
                operand=operand,
            )
        elif ctx.multOp():
            left, right = self._extract_left_right_vector_operations(ctx)
            context = ctx.multOp()
            op_codes = ("MOD", "DIV", "MULT")
            op = self._extract_op(context, op_codes)
            grouping = self._extract_grouping(grouping=context.grouping())
            return MultOpNode(
                ctx,
                left=left,
                right=right,
                operator=op.getText(),
                grouping=grouping,
                comments=self._extract_comments_from_context(context),
            )
        elif ctx.subqueryOp():
            subquery = self.visit(ctx.subqueryOp())
            assert len(ctx.vectorOperation()) == 1
            vector_op = ctx.vectorOperation()[0]
            left = self.visit(vector_op)
            return SubqueryNode(ctx, left=left, subquery_range=subquery)
        elif ctx.compareOp():
            context = ctx.compareOp()
            left, right = self._extract_left_right_vector_operations(ctx)
            op_codes = ("DEQ", "GT", "LT", "GE", "LE", "NE", "BOOL")
            op = self._extract_op(context, op_codes)
            grouping = self._extract_grouping(grouping=context.grouping())
            bool_keyword = None
            if context.BOOL():
                bool_keyword = context.BOOL().getText()
            return CompareOperationNode(
                context,
                left=left,
                right=right,
                operator=op.getText(),
                grouping=grouping,
                bool_keyword=bool_keyword,
                comments=self._extract_comments_from_context(context),
            )
        elif ctx.andUnlessOp():
            left, right = self._extract_left_right_vector_operations(ctx)
            context = ctx.andUnlessOp()
            op_codes = ("AND", "UNLESS")
            op = self._extract_op(context, op_codes)
            grouping = self._extract_grouping(grouping=context.grouping())
            return AndUnlessOperationNode(
                ctx,
                left=left,
                right=right,
                operator=op.getText(),
                grouping=grouping,
                comments=self._extract_comments_from_context(context),
            )
        elif ctx.orOp():
            left, right = self._extract_left_right_vector_operations(ctx)
            context = ctx.orOp()
            grouping = self._extract_grouping(grouping=context.grouping())
            return OrOperationNode(
                ctx,
                left=left,
                right=right,
                operator=context.OR().getText(),
                grouping=grouping,
                comments=self._extract_comments_from_context(context),
            )
        else:
            return self.visit(ctx.vector())

    def _extract_left_right_vector_operations(self, ctx):
        assert len(ctx.vectorOperation()) == 2
        left_op, right_op = ctx.vectorOperation()
        left = self.visit(left_op)
        right = self.visit(right_op)
        return left, right

    def _extract_grouping(self, grouping):
        if grouping is None:
            return None
        assert grouping.on_() or grouping.ignoring()
        on_ignoring = self.visitOnIgnoring(grouping)

        group_left_right = None
        if grouping.groupLeft():
            context = grouping.groupLeft()
            group_left_right = GroupLeftRight(
                ctx=context,
                operator="group_left",
                labels=self.visit(context.labelNameList()),
                comments=self._extract_comments_from_context(context),
            )
        elif grouping.groupRight():
            context = grouping.groupRight()
            group_left_right = GroupLeftRight(
                ctx=context,
                operator="group_right",
                labels=self.visit(context.labelNameList()),
                comments=self._extract_comments_from_context(context),
            )

        return Grouping(
            on_ignoring=on_ignoring,
            group_left_right=group_left_right,
        )

    def visitOnIgnoring(self, grouping):
        comments = self._extract_comments_from_context(grouping)
        if grouping.on_():
            context = grouping.on_()
            on_ignoring = OnIgnoring(
                ctx=context,
                operator=context.ON().getText(),
                labels=self.visit(context.labelNameList()),
                comments=comments,
            )
        else:
            context = grouping.ignoring()
            on_ignoring = OnIgnoring(
                ctx=context,
                operator=context.IGNORING().getText(),
                labels=self.visit(context.labelNameList()),
                comments=comments,
            )
        return on_ignoring

    def _extract_op(self, context, op_codes):
        for op_code in op_codes:
            op = getattr(context, op_code)()
            if op is not None:
                break
        else:
            raise Exception("Expected to find op but didn't")
        return op

    def visitSubqueryOp(self, ctx: PromQLParser.SubqueryOpContext):
        offset = None
        if ctx.offsetOp():
            offset = f"{ctx.offsetOp().OFFSET().getText()} {ctx.offsetOp().DURATION().getText()}"
        return SubqueryRangeNode(
            ctx,
            ctx.SUBQUERY_RANGE().getText(),
            offset=offset,
        )

    def visitVector(self, ctx: PromQLParser.VectorContext):
        if ctx.function_():
            return self.visit(ctx.function_())
        elif ctx.aggregation():
            return self.visit(ctx.aggregation())
        elif ctx.instantSelector():
            return self.visit(ctx.instantSelector())
        elif ctx.matrixSelector():
            return self.visit(ctx.matrixSelector())
        elif ctx.offset():
            return self.visit(ctx.offset())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.parens():
            return self.visit(ctx.parens())

    def visitOffset(self, ctx: PromQLParser.OffsetContext):
        selector = self.visit(ctx.instantSelector() or ctx.matrixSelector())
        return OffsetNode(
            ctx,
            instant_selector=selector,
            offset=ctx.OFFSET().getText(),
            duration=ctx.DURATION().getText(),
        )

    def visitParens(self, ctx: PromQLParser.ParensContext):
        vector_operation = self.visit(ctx.vectorOperation())
        return ParensNode(ctx, vector_operation=vector_operation)

    def visitAggregation(self, ctx: PromQLParser.AggregationContext):
        operator = ctx.AGGREGATION_OPERATOR().getText()
        by_without = None
        if ctx.byWithout():
            by_without = self.visit(ctx.byWithout())
        parameter_list = self.visit(ctx.parameterList())
        return AggregationNode(
            ctx=ctx,
            operator=operator,
            by_without=by_without,
            parameter_list=parameter_list,
            is_prefix=ctx.prefix is not None,
        )

    def visitByWithout(self, ctx: PromQLParser.ByWithoutContext):
        group_operator = None
        group_label_list = []
        if ctx.by():
            group_operator = ctx.by().BY().getText()
            group_label_list = self.visit(ctx.by().labelNameList())
        elif ctx.without():
            group_operator = ctx.without().WITHOUT().getText()
            group_label_list = self.visit(ctx.without().labelNameList())
        assert group_operator

        return ByWithoutNode(
            group_operator=group_operator,
            group_label_list=group_label_list,
            comments=self._extract_comments_from_context(ctx),
        )

    def visitParameterList(self, ctx: PromQLParser.ParameterListContext):
        parameters = []
        for param in ctx.parameter():
            value = self.visit(param)
            parameters.append(Parameter(value=value))
        return ParameterListNode(ctx=ctx, parameters=parameters)

    def visitMatrixSelector(self, ctx: PromQLParser.MatrixSelectorContext):
        if ctx.instantSelector():
            selector = self.visit(ctx.instantSelector())
            return MatrixSelectorNode(
                ctx=ctx,
                selector=selector,
                time_range=ctx.TIME_RANGE().getText(),
            )

    def visitInstantSelector(self, ctx: PromQLParser.InstantSelectorContext):
        labels = []
        if ctx.labelMatcherList():
            labels = self.visit(ctx.labelMatcherList())
        metric_name = ""
        if ctx.METRIC_NAME():
            metric_name = ctx.METRIC_NAME().getText()

        left_brace, right_brace = None, None
        if ctx.LEFT_BRACE() and ctx.RIGHT_BRACE():
            left_brace = ctx.LEFT_BRACE().getText()
            right_brace = ctx.RIGHT_BRACE().getText()
        return InstantSelectorNode(
            ctx,
            metric_name=metric_name,
            labels=labels,
            left_brace=left_brace,
            right_brace=right_brace,
        )

    def visitLabelMatcherList(self, ctx: PromQLParser.LabelMatcherListContext):
        labels = []
        for matcher in ctx.labelMatcher():
            labels.append(self.visit(matcher))
        has_trailing_comma = len(labels) == len(ctx.COMMA())
        return LabelList(ctx, labels=labels, has_trailing_comma=has_trailing_comma)

    def visitLabelNameList(self, ctx: PromQLParser.LabelNameListContext):
        labels = []
        for label in ctx.labelName():
            if label.METRIC_NAME():
                name = label.METRIC_NAME().getText()
            elif label.LABEL_NAME():
                name = label.LABEL_NAME().getText()
            else:
                name = label.keyword().getText()
            assert name is not None
            comments = self._extract_comments_from_context(label)
            labels.append(LabelNameNode(ctx, name=name, comments=comments))
        return LabelList(ctx, labels)

    def visitLabelMatcher(self, ctx: PromQLParser.LabelMatcherContext):
        comment_tokens = self._extract_comments_from_context(ctx)
        return LabelNode(ctx, comments=comment_tokens)

    def _extract_comments_from_context(self, ctx):
        stream: CommonTokenStream = ctx.parser.getInputStream()
        index = ctx.start.tokenIndex
        comment_tokens = stream.getHiddenTokensToLeft(index, channel=3)
        if comment_tokens:
            return [c.text.strip() for c in comment_tokens]

    def visitFunction_(self, ctx: PromQLParser.Function_Context):
        parameters = []
        for parameter in ctx.parameter():
            param = self.visit(parameter)
            if param is not None:
                parameters.append(Parameter(value=param))
        return FunctionNode(
            ctx=ctx,
            parameters=ParameterListNode(ctx, parameters=parameters),
        )

    def visitParameter(self, ctx: PromQLParser.ParameterContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.vectorOperation():
            return self.visit(ctx.vectorOperation())

    def visitLiteral(self, ctx: PromQLParser.LiteralContext):
        if ctx.NUMBER():
            return Number(ctx=ctx, value=ctx.getText())
        if ctx.STRING():
            return String(ctx=ctx, value=ctx.getText())


def skip_comment():
    def outer(func):
        func.skip_comment = True

        @functools.wraps(func)
        def inner(*args, **kwargs) -> None:
            return func(*args, **kwargs)

        return inner

    return outer


class PromQLFormatter:
    def __init__(self):
        self.indent = 0
        self.buffer: Optional[SmartBuffer] = None

    def format(self, tree):
        with SmartBuffer() as buff:
            self.buffer = buff
            self.visit(tree)
            return buff.getvalue()

    def visit(self, node):
        method_name = f"visit{type(node).__name__}"
        method = self.__getattribute__(method_name)
        if not hasattr(method, "skip_comment"):
            self._write_comments(node)
        result = method(node)
        return result

    def write(self, *output, suffix="", end=None):
        indent = "  " * self.indent
        if end is not None:
            indent = ""
        print(indent + " ".join(output) + suffix, end=end, file=self.buffer)

    def write_no_indent(self, *output):
        print(" ".join(output), file=self.buffer)

    @contextmanager
    def indent_block(self):
        self.indent += 1
        yield
        self.indent -= 1

    @contextmanager
    def no_indent(self):
        old_indent = self.indent
        self.indent = 0
        yield
        self.indent = old_indent

    def visitPowOpNode(self, node: PowOpNode):
        self._write_op_with_grouping(node)

    @skip_comment()
    def visitAddOpNode(self, node: AddOpNode):
        self._write_op_with_grouping(node)

    def visitUnaryOpNode(self, node: UnaryOpNode):
        self.write(node.operator, end="")
        self.visit(node.operand)

    @skip_comment()
    def visitMultOpNode(self, node: MultOpNode):
        self._write_op_with_grouping(node)

    @skip_comment()
    def visitOrOperationNode(self, node: OrOperationNode):
        self._write_op_with_grouping(node)

    @skip_comment()
    def visitCompareOperationNode(self, node: CompareOperationNode):
        self._write_op_with_grouping(node, bool_keyword=node.bool_keyword)

    @skip_comment()
    def visitAndUnlessOperationNode(self, node: AndUnlessOperationNode):
        self._write_op_with_grouping(node)

    def visitNumber(self, node: Number):
        self.write(node.value)

    def visitString(self, node: Number):
        self.write(node.value)

    def visitParensNode(self, node: ParensNode):
        self.write("(")
        with self.indent_block():
            self.visit(node.vector_operation)
        self.write(")")

    def visitOffsetNode(self, node: OffsetNode):
        self.visit(node.instant_selector)
        self.write(node.offset, node.duration)

    def visitFunctionNode(self, node: FunctionNode):
        self.write(node.name)
        self.visitParameterListNode(node.parameters)

    def visitAggregationNode(self, node: AggregationNode):
        self.write(node.operator)
        if node.is_prefix:
            if node.by_without:
                self.buffer.chomp_newline()
                self._write_comments(node.by_without)
                self.write_no_indent(node.by_without.group_operator, "(")
                with self.indent_block():
                    self._write_comma_seperated_list(
                        node.by_without.group_label_list,
                        format_func=lambda label: f"{label.name}",
                    )
                self.write(")")

        if node.parameter_list:
            self.visitParameterListNode(node.parameter_list)
        if not node.is_prefix:
            if node.by_without:
                self._write_comments(node.by_without)
                self.write(node.by_without.group_operator, "(")
                with self.indent_block():
                    self._write_comma_seperated_list(
                        node.by_without.group_label_list,
                        format_func=lambda label: f"{label.name}",
                    )
                self.write(")")

    def visitSubqueryNode(self, node: SubqueryNode):
        with self.indent_block():
            self.visit(node.left)
            self.visit(node.subquery_range)

    def visitMatrixSelectorNode(self, node: MatrixSelectorNode):
        self.visit(node.selector)
        self.buffer.chomp_newline()
        with self.no_indent():
            self.write(node.time_range)

    def visitInstantSelectorNode(self, node: InstantSelectorNode):
        self.write(node.metric_name)
        if node.left_brace:
            self.write(node.left_brace)
        if node.labels:
            with self.indent_block():
                self._write_comma_seperated_list(
                    node.labels,
                    format_func=lambda label: f"{label.name}{label.operator}{label.value}",
                )
        if node.right_brace:
            self.write(node.right_brace)

    def visitMetricNameNode(self, node: MetricNameNode):
        self.write(node.metric_name)

    def visitSubqueryRangeNode(self, node: SubqueryRangeNode):
        self.buffer.chomp_newline()
        with self.no_indent():
            offset = node.offset or ""
            self.write(node.subquery_range, end=None if offset else "")
            if offset:
                self.write(node.offset)

    def _write_op_with_grouping(self, node, bool_keyword=None):
        self.visit(node.left)
        self._write_comments(node)
        self.write(node.operator, suffix=" ", end=f"")
        if bool_keyword is not None:
            with self.no_indent():
                self.write(bool_keyword, end=" ")
        if node.grouping:
            self._write_comments(node.grouping.on_ignoring)
            self.write(node.grouping.on_ignoring.operator, "(")
            with self.indent_block():
                self._write_comma_seperated_list(
                    label_list=node.grouping.on_ignoring.labels,
                    format_func=lambda label: label.name,
                )
            self.write(")")
            if node.grouping.group_left_right:
                self._write_comments(node.grouping.group_left_right)
                self.write(node.grouping.group_left_right.operator, "(")
                with self.indent_block():
                    self._write_comma_seperated_list(
                        label_list=node.grouping.group_left_right.labels,
                        format_func=lambda label: label.name,
                    )
                self.write(")")
        with self.no_indent():
            self.visit(node.right)

    def visitParameterListNode(self, parameter_list: ParameterListNode):
        param_len = len(parameter_list.parameters)
        self._write_comments(parameter_list)
        self.write("(")
        for index, param in enumerate(parameter_list.parameters):
            with self.indent_block():
                self.visit(param.value)
                if index + 1 != param_len:
                    self.buffer.strip()
                    self.write_no_indent(",")
        self.write(")")

    def _write_comma_seperated_list(self, label_list: LabelList, format_func):
        self._write_comments(label_list)
        items_len = len(label_list.labels)
        for index, item in enumerate(label_list.labels, start=1):
            suffix = ","
            if index == items_len and not label_list.has_trailing_comma:
                suffix = ""
            output = format_func(item)
            self._write_comments(item)
            self.write(output, suffix=suffix)

    def _write_comments(self, item):
        if item.comments:
            for comment in item.comments:
                self.write(comment)
