from contextlib import contextmanager

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
)
from promformat.parser.PromQLParser import PromQLParser
from promformat.parser.PromQLParserVisitor import PromQLParserVisitor


class BuildAstVisitor(PromQLParserVisitor):
    def visit(self, tree):
        # print("visit -> ", type(tree).__name__)
        return super().visit(tree)

    def visitExpression(self, ctx: PromQLParser.ExpressionContext):
        return self.visit(ctx.vectorOperation())

    def visitVectorOperation(self, ctx: PromQLParser.VectorOperationContext):
        if ctx.powOp():
            assert len(ctx.vectorOperation()) == 2
            right_op, left_op = ctx.vectorOperation()
            left = self.visit(left_op)
            right = self.visit(right_op)
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
            assert len(ctx.vectorOperation()) == 2
            right_op, left_op = ctx.vectorOperation()
            left = self.visit(left_op)
            right = self.visit(right_op)
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
            assert len(ctx.vectorOperation()) == 2
            right_op, left_op = ctx.vectorOperation()
            left = self.visit(left_op)
            right = self.visit(right_op)
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
            assert len(ctx.vectorOperation()) == 2
            right_op, left_op = ctx.vectorOperation()
            left = self.visit(left_op)
            right = self.visit(right_op)
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
            assert len(ctx.vectorOperation()) == 2
            right_op, left_op = ctx.vectorOperation()
            left = self.visit(left_op)
            right = self.visit(right_op)
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
            assert len(ctx.vectorOperation()) == 2
            right_op, left_op = ctx.vectorOperation()
            left = self.visit(left_op)
            right = self.visit(right_op)
            grouping = self._extract_grouping(grouping=ctx.orOp().grouping())
            return OrOperationNode(
                ctx,
                left=left,
                right=right,
                grouping=grouping,
            )
        else:
            return self.visit(ctx.vector())

    def _extract_grouping(self, grouping):
        if grouping is None:
            return None
        assert grouping.on_() or grouping.ignoring()
        # assert grouping.groupLeft() or grouping.groupRight()
        if grouping.on_():
            operator = "on"
            label_name_list = self.visitLabelNameList(grouping.on_().labelNameList())
        else:
            operator = "ignoring"
            label_name_list = self.visitLabelNameList(
                grouping.ignoring().labelNameList()
            )
        on_ignoring = OnIgnoring(
            operator=operator,
            labels=label_name_list,
        )

        if grouping.groupLeft():
            operator = "group_left"
            label_name_list = self.visitLabelNameList(
                grouping.groupLeft().labelNameList()
            )
        elif grouping.groupRight():
            operator = "group_right"
            label_name_list = self.visitLabelNameList(
                grouping.groupRight().labelNameList()
            )
        group_left_right = GroupLeftRight(
            operator=operator,
            labels=label_name_list,
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
        print("OFFSET", ctx)
        assert False

    def visitParens(self, ctx: PromQLParser.ParensContext):
        vector_operation = self.visit(ctx.vectorOperation())
        return ParensNode(ctx, vector_operation=vector_operation)

    def visitAggregation(self, ctx: PromQLParser.AggregationContext):
        operator = ctx.AGGREGATION_OPERATOR().getText()
        if ctx.by():
            group_operator = ctx.by().BY().getText()
            group_label_list = self.visitLabelNameList(ctx.by().labelNameList())
        elif ctx.without():
            group_operator = ctx.without().WITHOUT.getText()
            group_label_list = self.visitLabelNameList(ctx.without().labelNameList())
        else:
            group_operator = None
            group_label_list = []
        parameter_list = self.visit(ctx.parameterList())
        return AggregationNode(
            ctx=ctx,
            operator=operator,
            group_operator=group_operator,
            label_list=group_label_list,
            parameter_list=parameter_list,
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
        metric_name = ctx.METRIC_NAME().getText()
        return InstantSelectorNode(
            ctx,
            metric_name=metric_name,
            labels=labels,
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
            parameters.append(self.visit(parameter))
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


class AstFormatterVisitor:
    def __init__(self):
        self.indent = 0

    def write(self, *output, suffix="", end=None):
        indent = "  " * self.indent
        print(indent + " ".join(output) + suffix, end=end)

    @contextmanager
    def indent_block(self):
        self.indent += 1
        yield
        self.indent -= 1

    def visitPowOpNode(self, node: PowOpNode):
        self._write_op_with_grouping(node)

    def _write_op_with_grouping(self, node):
        self.visit(node.right)
        self.write(node.operator)
        if node.grouping:
            self.write(node.grouping.on_ignoring.operator, "(")
            with self.indent_block():
                for label in node.grouping.on_ignoring.labels:
                    self.write(label.name, suffix=",")
            self.write(")")
            if node.grouping.group_left_right:
                self.write(node.grouping.group_left_right.operator, "(")
                with self.indent_block():
                    for label in node.grouping.group_left_right.labels:
                        self.write(label.name, suffix=",")
                self.write(")")
        self.visit(node.left)

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

    def visitFunctionNode(self, node: FunctionNode):
        self.write(node.name, "(")
        param_len = len(node.parameters)
        for index, param in enumerate(node.parameters):
            with self.indent_block():
                self.visit(param)
                if index + 1 != param_len:
                    self.write(",", end="")
        self.write(")")

    def visitAggregationNode(self, node: AggregationNode):
        if node.group_operator:
            self.write(node.operator, node.group_operator, "(")
            with self.indent_block():
                for label in node.label_list:
                    self.write(label.name, suffix=",")
            self.write(")")
        else:
            self.write(node.operator)
        if node.parameter_list:
            self.write("(")
            for param in node.parameter_list:
                with self.indent_block():
                    self.visit(param)
            self.write(")")

    def visitSubqueryNode(self, node: SubqueryNode):
        with self.indent_block():
            self.write("(")
            self.visit(node.left)
            self.write(")")
            self.write(node.subquery_range.subquery_range)

    def visitMatrixSelectorNode(self, node: MatrixSelectorNode):
        self.write(node.selector.metric_name)
        if node.selector.labels:
            self.write("{")
            for label in node.selector.labels:
                with self.indent_block():
                    self.write(f"{label.name}{label.operator}{label.value}", suffix=",")
            self.write("}")
        self.write(node.time_range, end="")

    def visitInstantSelectorNode(self, node: InstantSelectorNode):
        self.write(node.metric_name)
        if node.labels:
            self.write("{")
            for label in node.labels:
                with self.indent_block():
                    self.write(f"{label.name}{label.operator}{label.value}", suffix=",")
            self.write("}")

    def visitMetricNameNode(self, node: MetricNameNode):
        self.write(node.metric_name)

    def visit(self, node):
        method_name = f"visit{type(node).__name__}"
        method = self.__getattribute__(method_name)
        result = method(node)
        return result
