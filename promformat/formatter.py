from contextlib import contextmanager
from io import StringIO

from antlr4 import ErrorNode, TerminalNode

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
)
from promformat.error import UnEqualParseTreeError
from promformat.parser.PromQLParser import PromQLParser
from promformat.parser.PromQLParserVisitor import PromQLParserVisitor


class ParseTreeValidator:
    def validate(self, left, right):
        if type(left) != type(right):
            raise UnEqualParseTreeError(
                f"Expected: {type(left).__name__}, found: {type(right).__name__}"
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
        sentinel = object
        assert next(left_children, sentinel) == next(right_children, sentinel)


class BuildAstVisitor(PromQLParserVisitor):
    def visit(self, tree):
        # print("visit -> ", type(tree).__name__)
        return super().visit(tree)

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
            grouping = self._extract_grouping(grouping=ctx.addOp().grouping())
            return AddOpNode(
                ctx,
                left=left,
                right=right,
                operator=op.getText(),
                grouping=grouping,
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
            grouping = self._extract_grouping(grouping=ctx.multOp().grouping())
            return MultOpNode(
                ctx,
                left=left,
                right=right,
                operator=op.getText(),
                grouping=grouping,
            )
        elif ctx.subqueryOp():
            subquery = self.visit(ctx.subqueryOp())
            assert len(ctx.vectorOperation()) == 1
            vector_op = ctx.vectorOperation()[0]
            left = self.visit(vector_op)
            return SubqueryNode(ctx, left=left, subquery_range=subquery)
        elif ctx.compareOp():
            left, right = self._extract_left_right_vector_operations(ctx)
            context = ctx.compareOp()
            op_codes = ("DEQ", "GT", "LT", "GE", "LE", "NE", "BOOL")
            op = self._extract_op(context, op_codes)
            grouping = self._extract_grouping(grouping=ctx.compareOp().grouping())
            return CompareOperationNode(
                ctx,
                left=left,
                right=right,
                operator=op.getText(),
                grouping=grouping,
            )
        elif ctx.andUnlessOp():
            left, right = self._extract_left_right_vector_operations(ctx)
            context = ctx.andUnlessOp()
            op_codes = ("AND", "UNLESS")
            op = self._extract_op(context, op_codes)
            grouping = self._extract_grouping(grouping=ctx.andUnlessOp().grouping())
            return AndUnlessOperationNode(
                ctx,
                left=left,
                right=right,
                operator=op.getText(),
                grouping=grouping,
            )
        elif ctx.orOp():
            left, right = self._extract_left_right_vector_operations(ctx)
            grouping = self._extract_grouping(grouping=ctx.orOp().grouping())
            return OrOperationNode(
                ctx,
                left=left,
                right=right,
                grouping=grouping,
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
        if grouping.on_():
            on_ignoring = OnIgnoring(
                operator="on",
                labels=self.visitLabelNameList(grouping.on_().labelNameList()),
            )
        else:
            on_ignoring = OnIgnoring(
                operator="ignoring",
                labels=self.visitLabelNameList(grouping.ignoring().labelNameList()),
            )

        group_left_right = None
        if grouping.groupLeft():
            group_left_right = GroupLeftRight(
                operator="group_left",
                labels=self.visitLabelNameList(grouping.groupLeft().labelNameList()),
            )
        elif grouping.groupRight():
            group_left_right = GroupLeftRight(
                operator="group_right",
                labels=self.visitLabelNameList(grouping.groupRight().labelNameList()),
            )

        return Grouping(
            on_ignoring=on_ignoring,
            group_left_right=group_left_right,
        )

    def _extract_op(self, context, op_codes):
        for op_code in op_codes:
            op = getattr(context, op_code)()
            if op is not None:
                break
        else:
            raise Exception("Expected to find op but didn't")
        return op

    def visitSubqueryOp(self, ctx: PromQLParser.SubqueryOpContext):
        return SubqueryRangeNode(ctx, ctx.SUBQUERY_RANGE().getText())

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
        print("visitVector")

    def visitOffset(self, ctx: PromQLParser.OffsetContext):
        selector = self.visit(ctx.instantSelector())
        return OffsetNode(
            ctx,
            instant_selector=selector,
            duration=ctx.DURATION().getText(),
        )

    def visitParens(self, ctx: PromQLParser.ParensContext):
        vector_operation = self.visit(ctx.vectorOperation())
        return ParensNode(ctx, vector_operation=vector_operation)

    def visitAggregation(self, ctx: PromQLParser.AggregationContext):
        operator = ctx.AGGREGATION_OPERATOR().getText()
        if ctx.byWithout() is None:
            group_operator = None
            group_label_list = []
        elif ctx.byWithout().by():
            group_operator = ctx.byWithout().by().BY().getText()
            group_label_list = self.visitLabelNameList(
                ctx.byWithout().by().labelNameList()
            )
        elif ctx.byWithout().without():
            group_operator = ctx.byWithout().without().WITHOUT().getText()
            group_label_list = self.visitLabelNameList(
                ctx.byWithout().without().labelNameList()
            )

        parameter_list = self.visit(ctx.parameterList())
        return AggregationNode(
            ctx=ctx,
            operator=operator,
            group_operator=group_operator,
            label_list=group_label_list,
            parameter_list=parameter_list,
            is_prefix=ctx.prefix is not None,
        )

    def visitParameterList(self, ctx: PromQLParser.ParameterListContext):
        parameters = []
        for param in ctx.parameter():
            parameters.append(self.visit(param))
        return parameters

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
        return labels

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
            labels.append(LabelNameNode(ctx, name=name))
        return labels

    def visitLabelMatcher(self, ctx: PromQLParser.LabelMatcherContext):
        return LabelNode(ctx)

    def visitFunction_(self, ctx: PromQLParser.Function_Context):
        parameters = []
        for parameter in ctx.parameter():
            param = self.visit(parameter)
            if param is not None:
                parameters.append(param)
        return FunctionNode(ctx=ctx, parameters=parameters)

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


class PromQLFormatter:
    def __init__(self):
        self.indent = 0
        self.buffer = None

    def format(self, tree):
        with StringIO() as buff:
            self.buffer = buff
            self.visit(tree)
            return buff.getvalue()

    def visit(self, node):
        method_name = f"visit{type(node).__name__}"
        method = self.__getattribute__(method_name)
        result = method(node)
        return result

    def write(self, *output, suffix="", end=None):
        indent = "  " * self.indent
        print(indent + " ".join(output) + suffix, end=end, file=self.buffer)

    @contextmanager
    def indent_block(self):
        self.indent += 1
        yield
        self.indent -= 1

    def visitPowOpNode(self, node: PowOpNode):
        self._write_op_with_grouping(node)

    def visitAddOpNode(self, node: AddOpNode):
        self._write_op_with_grouping(node)

    def visitUnaryOpNode(self, node: UnaryOpNode):
        self.write(node.operator, end="")
        self.visit(node.operand)

    def visitMultOpNode(self, node: MultOpNode):
        self._write_op_with_grouping(node)

    def visitOrOperationNode(self, node: OrOperationNode):
        self._write_op_with_grouping(node)

    def visitCompareOperationNode(self, node: CompareOperationNode):
        self._write_op_with_grouping(node)

    def visitAndUnlessOperationNode(self, node: AndUnlessOperationNode):
        self._write_op_with_grouping(node)

    def visitNumber(self, node: Number):
        self.write(node.value)

    def visitString(self, node: Number):
        self.write(node.value)

    def visitParensNode(self, node: ParensNode):
        self.write("(")
        self.visit(node.vector_operation)
        self.write(")")

    def visitOffsetNode(self, node: OffsetNode):
        self.visit(node.instant_selector)
        self.write("offset", node.duration)

    def visitFunctionNode(self, node: FunctionNode):
        self.write(node.name, "(")
        self._write_parameter_list(node.parameters)
        self.write(")")

    def visitAggregationNode(self, node: AggregationNode):
        self.write(node.operator)
        if node.is_prefix:
            if node.group_operator:
                self.write(node.group_operator, "(")
                with self.indent_block():
                    self._write_comma_seperated_list(
                        node.label_list,
                        format_func=lambda label: f"{label.name}",
                    )
                self.write(")")

        if node.parameter_list:
            self.write("(")
            self._write_parameter_list(node.parameter_list)
            self.write(")")
        if not node.is_prefix:
            if node.group_operator:
                self.write(node.group_operator, "(")
                with self.indent_block():
                    self._write_comma_seperated_list(
                        node.label_list,
                        format_func=lambda label: f"{label.name}",
                    )
                self.write(")")

    def visitSubqueryNode(self, node: SubqueryNode):
        with self.indent_block():
            self.visit(node.left)
            self.write(node.subquery_range.subquery_range)

    def visitMatrixSelectorNode(self, node: MatrixSelectorNode):
        self.write(node.selector.metric_name)
        if node.selector.left_brace:
            self.write(node.selector.left_brace)
        if node.selector.labels:
            with self.indent_block():
                self._write_comma_seperated_list(
                    node.selector.labels,
                    format_func=lambda label: f"{label.name}{label.operator}{label.value}",
                )
        if node.selector.right_brace:
            self.write(node.selector.right_brace)
        self.write(node.time_range, end="")

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

    def _write_op_with_grouping(self, node):
        self.visit(node.left)
        self.write(node.operator, end="", suffix=" ")
        if node.grouping:
            self.write(node.grouping.on_ignoring.operator, "(")
            with self.indent_block():
                self._write_comma_seperated_list(
                    items=node.grouping.on_ignoring.labels,
                    format_func=lambda label: label.name,
                )
            self.write(")")
            if node.grouping.group_left_right:
                self.write(node.grouping.group_left_right.operator, "(")
                with self.indent_block():
                    self._write_comma_seperated_list(
                        items=node.grouping.group_left_right.labels,
                        format_func=lambda label: label.name,
                    )
                self.write(")")
        self.visit(node.right)

    def _write_parameter_list(self, parameter_list):
        param_len = len(parameter_list)
        for index, param in enumerate(parameter_list):
            with self.indent_block():
                self.visit(param)
                if index + 1 != param_len:
                    self.write(",", end="")

    def _write_comma_seperated_list(self, items, format_func):
        items_len = len(items)
        for index, item in enumerate(items, start=1):
            suffix = "," if index != items_len else ""
            output = format_func(item)
            self.write(output, suffix=suffix)
