# Generated from PromQLParser.g4 by ANTLR 4.10
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .PromQLParser import PromQLParser
else:
    from PromQLParser import PromQLParser

# This class defines a complete generic visitor for a parse tree produced by PromQLParser.


class PromQLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PromQLParser#expression.
    def visitExpression(self, ctx: PromQLParser.ExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#vectorOperation.
    def visitVectorOperation(self, ctx: PromQLParser.VectorOperationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#unaryOp.
    def visitUnaryOp(self, ctx: PromQLParser.UnaryOpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#powOp.
    def visitPowOp(self, ctx: PromQLParser.PowOpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#multOp.
    def visitMultOp(self, ctx: PromQLParser.MultOpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#addOp.
    def visitAddOp(self, ctx: PromQLParser.AddOpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#compareOp.
    def visitCompareOp(self, ctx: PromQLParser.CompareOpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#andUnlessOp.
    def visitAndUnlessOp(self, ctx: PromQLParser.AndUnlessOpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#orOp.
    def visitOrOp(self, ctx: PromQLParser.OrOpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#vectorMatchOp.
    def visitVectorMatchOp(self, ctx: PromQLParser.VectorMatchOpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#subqueryOp.
    def visitSubqueryOp(self, ctx: PromQLParser.SubqueryOpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#offsetOp.
    def visitOffsetOp(self, ctx: PromQLParser.OffsetOpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#vector.
    def visitVector(self, ctx: PromQLParser.VectorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#parens.
    def visitParens(self, ctx: PromQLParser.ParensContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#instantSelector.
    def visitInstantSelector(self, ctx: PromQLParser.InstantSelectorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#labelMatcher.
    def visitLabelMatcher(self, ctx: PromQLParser.LabelMatcherContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#labelMatcherOperator.
    def visitLabelMatcherOperator(self, ctx: PromQLParser.LabelMatcherOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#labelMatcherList.
    def visitLabelMatcherList(self, ctx: PromQLParser.LabelMatcherListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#matrixSelector.
    def visitMatrixSelector(self, ctx: PromQLParser.MatrixSelectorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#offset.
    def visitOffset(self, ctx: PromQLParser.OffsetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#function_.
    def visitFunction_(self, ctx: PromQLParser.Function_Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#parameter.
    def visitParameter(self, ctx: PromQLParser.ParameterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#parameterList.
    def visitParameterList(self, ctx: PromQLParser.ParameterListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#aggregation.
    def visitAggregation(self, ctx: PromQLParser.AggregationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#by.
    def visitBy(self, ctx: PromQLParser.ByContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#without.
    def visitWithout(self, ctx: PromQLParser.WithoutContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#byWithout.
    def visitByWithout(self, ctx: PromQLParser.ByWithoutContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#grouping.
    def visitGrouping(self, ctx: PromQLParser.GroupingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#on_.
    def visitOn_(self, ctx: PromQLParser.On_Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#ignoring.
    def visitIgnoring(self, ctx: PromQLParser.IgnoringContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#groupLeft.
    def visitGroupLeft(self, ctx: PromQLParser.GroupLeftContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#groupRight.
    def visitGroupRight(self, ctx: PromQLParser.GroupRightContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#labelName.
    def visitLabelName(self, ctx: PromQLParser.LabelNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#labelNameList.
    def visitLabelNameList(self, ctx: PromQLParser.LabelNameListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#keyword.
    def visitKeyword(self, ctx: PromQLParser.KeywordContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PromQLParser#literal.
    def visitLiteral(self, ctx: PromQLParser.LiteralContext):
        return self.visitChildren(ctx)


del PromQLParser
