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


class ParensNode(Expr):
    def __init__(self, ctx, vector_operation):
        super(ParensNode, self).__init__(ctx)
        self.vector_operation = vector_operation


class UnaryOpNode(Expr):
    def __init__(self, ctx, operator, operand):
        super(UnaryOpNode, self).__init__(ctx)
        self.operator = operator
        self.operand = operand


class PowOpNode(Expr):
    def __init__(self, ctx, left, right, operator, grouping):
        super(PowOpNode, self).__init__(ctx)
        self.left = left
        self.right = right
        self.operator = operator
        self.grouping = grouping


class AddOpNode(Expr):
    def __init__(self, ctx, left, right, operator, grouping):
        super(AddOpNode, self).__init__(ctx)
        self.left = left
        self.right = right
        self.operator = operator
        self.grouping = grouping


class MultOpNode(Expr):
    def __init__(self, ctx, left, right, operator, grouping):
        super(MultOpNode, self).__init__(ctx)
        self.left = left
        self.right = right
        self.operator = operator
        self.grouping = grouping


class CompareOperationNode(Expr):
    def __init__(
        self,
        ctx,
        left,
        right,
        operator,
        grouping,
        bool_keyword,
    ):
        super(CompareOperationNode, self).__init__(ctx)
        self.left = left
        self.right = right
        self.operator = operator
        self.grouping = grouping
        self.bool_keyword = bool_keyword


class OnIgnoring:
    def __init__(self, operator, labels):
        self.operator = operator
        self.labels = labels


class GroupLeftRight:
    def __init__(self, operator, labels):
        self.operator = operator
        self.labels = labels


class Grouping:
    def __init__(self, on_ignoring, group_left_right):
        self.on_ignoring = on_ignoring
        self.group_left_right = group_left_right


class AndUnlessOperationNode(Expr):
    def __init__(self, ctx, left, right, operator, grouping):
        super(AndUnlessOperationNode, self).__init__(ctx)
        self.left = left
        self.right = right
        self.operator = operator
        self.grouping = grouping


class OrOperationNode(Expr):
    def __init__(self, ctx, left, right, operator, grouping):
        super(OrOperationNode, self).__init__(ctx)
        self.left = left
        self.right = right
        self.operator = operator
        self.grouping = grouping


class LabelNode(Expr):
    def __init__(self, ctx: PromQLParser.LabelMatcherContext):
        super(LabelNode, self).__init__(ctx)
        self.name = ctx.labelName().getText()
        self.operator = ctx.labelMatcherOperator().getText()
        self.value = ctx.STRING().getText()


class OffsetNode(Expr):
    def __init__(self, ctx, instant_selector, offset, duration):
        super(OffsetNode, self).__init__(ctx)
        self.instant_selector = instant_selector
        self.offset = offset
        self.duration = duration


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
    def __init__(
        self, ctx, metric_name: str, labels: List[LabelNode], left_brace, right_brace
    ):
        super(InstantSelectorNode, self).__init__(ctx)
        self.metric_name = metric_name
        self.labels = labels
        self.left_brace = left_brace
        self.right_brace = right_brace


class SubqueryRangeNode(Expr):
    def __init__(self, ctx, subquery_range: str, offset):
        super(SubqueryRangeNode, self).__init__(ctx=ctx)
        self.subquery_range = subquery_range
        self.offset = offset


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
        self,
        ctx,
        operator: str,
        group_operator: str,
        label_list,
        parameter_list,
        is_prefix,
    ):
        super(AggregationNode, self).__init__(ctx)
        self.operator = operator
        self.group_operator = group_operator
        self.label_list = label_list
        self.parameter_list = parameter_list
        self.is_prefix = is_prefix


class MetricNameNode(Expr):
    def __init__(self, ctx, metric_name):
        super(MetricNameNode, self).__init__(ctx)
        self.metric_name = metric_name


class FunctionNode:
    def __init__(self, ctx: PromQLParser.Function_Context, parameters):
        self.ctx = ctx
        self.parameters = parameters
        self.name = self.ctx.FUNCTION().getText()
