from typing import List

from promformat.parser.PromQLParser import PromQLParser


class Expr:
    def __init__(self, ctx):
        self.ctx = ctx


class Literal(Expr):
    def __init__(self, ctx, value):
        super(Literal, self).__init__(ctx)
        self.value = value


class Number(Literal):
    pass


class String(Literal):
    pass


class UnaryOpNode(Expr):
    def __init__(self, ctx, operator, operand):
        super(UnaryOpNode, self).__init__(ctx)
        self.operator = operator
        self.operand = operand


class AddOpNode(Expr):
    def __init__(self, ctx, left, right, operator):
        super(AddOpNode, self).__init__(ctx)
        self.left = left
        self.right = right
        self.operator = operator


class MultOpNode(Expr):
    def __init__(self, ctx, left, right, operator):
        super(MultOpNode, self).__init__(ctx)
        self.left = left
        self.right = right
        self.operator = operator


class CompareOperationNode(Expr):
    def __init__(self, ctx, left, right, operator):
        super(CompareOperationNode, self).__init__(ctx)
        self.left = left
        self.right = right
        self.operator = operator


class AndUnlessOperationNode(Expr):
    def __init__(self, ctx, left, right, operator):
        super(AndUnlessOperationNode, self).__init__(ctx)
        self.left = left
        self.right = right
        self.operator = operator


class OrOperationNode(Expr):
    def __init__(self, ctx, left, right):
        super(OrOperationNode, self).__init__(ctx)
        self.left = left
        self.right = right
        self.operator = "or"


class LabelNode(Expr):
    def __init__(self, ctx: PromQLParser.LabelMatcherContext):
        super(LabelNode, self).__init__(ctx)
        self.name = ctx.labelName().getText()
        self.operator = ctx.labelMatcherOperator().getText()
        self.value = ctx.STRING().getText()


class LabelNameNode(Expr):
    def __init__(self, ctx, name: str):
        super(LabelNameNode, self).__init__(ctx)
        self.name = name


class LabelMatcherNode(Expr):
    def __init__(self, ctx, labels: List[LabelNode]):
        super(LabelMatcherNode, self).__init__(ctx)
        self.labels = labels

    def __len__(self):
        return len(self.labels)


class InstantSelectorNode(Expr):
    def __init__(self, ctx, metric_name: str, labels: List[LabelNode]):
        super(InstantSelectorNode, self).__init__(ctx)
        self.metric_name = metric_name
        self.labels = labels


class SubqueryRangeNode(Expr):
    def __init__(self, ctx, subquery_range: str):
        super(SubqueryRangeNode, self).__init__(ctx=ctx)
        self.subquery_range = subquery_range


class SubqueryNode(Expr):
    def __init__(self, ctx, left, subquery_range):
        super(SubqueryNode, self).__init__(ctx)
        self.left = left
        self.subquery_range = subquery_range


class MatrixSelectorNode(Expr):
    def __init__(self, ctx, selector: InstantSelectorNode, time_range):
        super(MatrixSelectorNode, self).__init__(ctx)
        self.selector = selector
        self.time_range = time_range


class AggregationNode(Expr):
    def __init__(
        self, ctx, operator: str, group_operator: str, label_list, parameter_list
    ):
        super(AggregationNode, self).__init__(ctx)
        self.operator = operator
        self.group_operator = group_operator
        self.label_list = label_list
        self.parameter_list = parameter_list


class MetricNameNode(Expr):
    def __init__(self, ctx, metric_name):
        super(MetricNameNode, self).__init__(ctx)
        self.metric_name = metric_name


class FunctionNode:
    def __init__(self, ctx: PromQLParser.Function_Context, parameters):
        self.ctx = ctx
        self.parameters = parameters
        self.name = self.ctx.FUNCTION().getText()
