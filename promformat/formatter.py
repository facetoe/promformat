from contextlib import contextmanager

from promformat.ast_nodes import (
    Number,
    MultiplicationNode,
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
        if ctx.multOp():
            left, right = ctx.vectorOperation()
            left_node = self.visit(left.vector())
            right_node = self.visit(right.vector())
            return MultiplicationNode(ctx, left_node, right_node)
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
            for op_code in ("GT", "LT", "GE", "LE", "BOOL"):
                op = getattr(ctx.compareOp(), op_code)()
                if op is not None:
                    break
            else:
                raise Exception("Expected to find op but didn't")
            return CompareOperationNode(
                ctx, left=left, right=right, operator=op.getText()
            )
        else:
            object_methods = [
                method_name
                for method_name in dir(ctx)
                if callable(getattr(ctx, method_name))
            ]
            for method_name in object_methods:
                if method_name.endswith("Op"):
                    res = getattr(ctx, method_name)()
                    if res is not None:
                        print(method_name, res)
            return self.visit(ctx.vector())

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

    def visitParens(self, ctx: PromQLParser.ParensContext):
        return self.visit(ctx.vectorOperation())

    def visitAggregation(self, ctx: PromQLParser.AggregationContext):
        operator = ctx.AGGREGATION_OPERATOR().getText()
        if ctx.by():
            group_operator = ctx.by().BY().getText()
            group_label_list = self.visitLabelNameList(ctx.by().labelNameList())
        elif ctx.without():
            group_operator = ctx.without().WITHOUT.getText()
            group_label_list = self.visitLabelNameList(ctx.without().labelNameList())
        else:
            raise Exception("BAD")
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
        # print(ctx.instantSelector().getText())
        # print(ctx.TIME_RANGE())

    def visitInstantSelector(self, ctx: PromQLParser.InstantSelectorContext):
        if ctx.labelMatcherList():
            labels = self.visit(ctx.labelMatcherList())
            metric_name = ctx.METRIC_NAME().getText()
            return InstantSelectorNode(
                ctx,
                metric_name=metric_name,
                labels=labels,
            )
        return MetricNameNode(ctx, ctx.METRIC_NAME().getText())

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
                name = label.keyword()
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


class Block:
    def __init__(self, open, close):
        self.open = open
        self.close = close


class Parentheses(Block):
    def __init__(self):
        super(Parentheses, self).__init__(open="(", close=")")


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

    def visitMultiplicationNode(self, node: MultiplicationNode):
        return f"{node.left.format()} * {node.right.format()}"

    def visitCompareOperationNode(self, node: CompareOperationNode):
        self.visit(node.right)
        self.write(f"{node.operator} ", end="")
        self.visit(node.left)

    def visitNumber(self, node: Number):
        self.write(str(node.value))

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
        self.write(node.operator, node.group_operator, "(")
        with self.indent_block():
            for label in node.label_list:
                self.write(label.name, suffix=",")
        self.write(")")
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
        self.write(node.selector.metric_name, "{")
        for label in node.selector.labels:
            with self.indent_block():
                self.write(f"{label.name}{label.operator}{label.value}", suffix=",")
        self.write("}", node.time_range)

    def visitMetricNameNode(self, node: MetricNameNode):
        self.write(node.metric_name)

    def visit(self, node):
        method_name = f"visit{type(node).__name__}"
        method = self.__getattribute__(method_name)
        result = method(node)
        # print(method_name, "->", self.indent)
        return result
