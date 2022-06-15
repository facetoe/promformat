# Generated from PromQLParser.g4 by ANTLR 4.10
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .PromQLParser import PromQLParser
else:
    from PromQLParser import PromQLParser

# This class defines a complete listener for a parse tree produced by PromQLParser.
class PromQLParserListener(ParseTreeListener):

    # Enter a parse tree produced by PromQLParser#expression.
    def enterExpression(self, ctx: PromQLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PromQLParser#expression.
    def exitExpression(self, ctx: PromQLParser.ExpressionContext):
        pass

    # Enter a parse tree produced by PromQLParser#vectorOperation.
    def enterVectorOperation(self, ctx: PromQLParser.VectorOperationContext):
        pass

    # Exit a parse tree produced by PromQLParser#vectorOperation.
    def exitVectorOperation(self, ctx: PromQLParser.VectorOperationContext):
        pass

    # Enter a parse tree produced by PromQLParser#unaryOp.
    def enterUnaryOp(self, ctx: PromQLParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by PromQLParser#unaryOp.
    def exitUnaryOp(self, ctx: PromQLParser.UnaryOpContext):
        pass

    # Enter a parse tree produced by PromQLParser#powOp.
    def enterPowOp(self, ctx: PromQLParser.PowOpContext):
        pass

    # Exit a parse tree produced by PromQLParser#powOp.
    def exitPowOp(self, ctx: PromQLParser.PowOpContext):
        pass

    # Enter a parse tree produced by PromQLParser#multOp.
    def enterMultOp(self, ctx: PromQLParser.MultOpContext):
        pass

    # Exit a parse tree produced by PromQLParser#multOp.
    def exitMultOp(self, ctx: PromQLParser.MultOpContext):
        pass

    # Enter a parse tree produced by PromQLParser#addOp.
    def enterAddOp(self, ctx: PromQLParser.AddOpContext):
        pass

    # Exit a parse tree produced by PromQLParser#addOp.
    def exitAddOp(self, ctx: PromQLParser.AddOpContext):
        pass

    # Enter a parse tree produced by PromQLParser#compareOp.
    def enterCompareOp(self, ctx: PromQLParser.CompareOpContext):
        pass

    # Exit a parse tree produced by PromQLParser#compareOp.
    def exitCompareOp(self, ctx: PromQLParser.CompareOpContext):
        pass

    # Enter a parse tree produced by PromQLParser#andUnlessOp.
    def enterAndUnlessOp(self, ctx: PromQLParser.AndUnlessOpContext):
        pass

    # Exit a parse tree produced by PromQLParser#andUnlessOp.
    def exitAndUnlessOp(self, ctx: PromQLParser.AndUnlessOpContext):
        pass

    # Enter a parse tree produced by PromQLParser#orOp.
    def enterOrOp(self, ctx: PromQLParser.OrOpContext):
        pass

    # Exit a parse tree produced by PromQLParser#orOp.
    def exitOrOp(self, ctx: PromQLParser.OrOpContext):
        pass

    # Enter a parse tree produced by PromQLParser#vectorMatchOp.
    def enterVectorMatchOp(self, ctx: PromQLParser.VectorMatchOpContext):
        pass

    # Exit a parse tree produced by PromQLParser#vectorMatchOp.
    def exitVectorMatchOp(self, ctx: PromQLParser.VectorMatchOpContext):
        pass

    # Enter a parse tree produced by PromQLParser#subqueryOp.
    def enterSubqueryOp(self, ctx: PromQLParser.SubqueryOpContext):
        pass

    # Exit a parse tree produced by PromQLParser#subqueryOp.
    def exitSubqueryOp(self, ctx: PromQLParser.SubqueryOpContext):
        pass

    # Enter a parse tree produced by PromQLParser#offsetOp.
    def enterOffsetOp(self, ctx: PromQLParser.OffsetOpContext):
        pass

    # Exit a parse tree produced by PromQLParser#offsetOp.
    def exitOffsetOp(self, ctx: PromQLParser.OffsetOpContext):
        pass

    # Enter a parse tree produced by PromQLParser#vector.
    def enterVector(self, ctx: PromQLParser.VectorContext):
        pass

    # Exit a parse tree produced by PromQLParser#vector.
    def exitVector(self, ctx: PromQLParser.VectorContext):
        pass

    # Enter a parse tree produced by PromQLParser#parens.
    def enterParens(self, ctx: PromQLParser.ParensContext):
        pass

    # Exit a parse tree produced by PromQLParser#parens.
    def exitParens(self, ctx: PromQLParser.ParensContext):
        pass

    # Enter a parse tree produced by PromQLParser#instantSelector.
    def enterInstantSelector(self, ctx: PromQLParser.InstantSelectorContext):
        pass

    # Exit a parse tree produced by PromQLParser#instantSelector.
    def exitInstantSelector(self, ctx: PromQLParser.InstantSelectorContext):
        pass

    # Enter a parse tree produced by PromQLParser#labelMatcher.
    def enterLabelMatcher(self, ctx: PromQLParser.LabelMatcherContext):
        pass

    # Exit a parse tree produced by PromQLParser#labelMatcher.
    def exitLabelMatcher(self, ctx: PromQLParser.LabelMatcherContext):
        pass

    # Enter a parse tree produced by PromQLParser#labelMatcherOperator.
    def enterLabelMatcherOperator(self, ctx: PromQLParser.LabelMatcherOperatorContext):
        pass

    # Exit a parse tree produced by PromQLParser#labelMatcherOperator.
    def exitLabelMatcherOperator(self, ctx: PromQLParser.LabelMatcherOperatorContext):
        pass

    # Enter a parse tree produced by PromQLParser#labelMatcherList.
    def enterLabelMatcherList(self, ctx: PromQLParser.LabelMatcherListContext):
        pass

    # Exit a parse tree produced by PromQLParser#labelMatcherList.
    def exitLabelMatcherList(self, ctx: PromQLParser.LabelMatcherListContext):
        pass

    # Enter a parse tree produced by PromQLParser#matrixSelector.
    def enterMatrixSelector(self, ctx: PromQLParser.MatrixSelectorContext):
        pass

    # Exit a parse tree produced by PromQLParser#matrixSelector.
    def exitMatrixSelector(self, ctx: PromQLParser.MatrixSelectorContext):
        pass

    # Enter a parse tree produced by PromQLParser#offset.
    def enterOffset(self, ctx: PromQLParser.OffsetContext):
        pass

    # Exit a parse tree produced by PromQLParser#offset.
    def exitOffset(self, ctx: PromQLParser.OffsetContext):
        pass

    # Enter a parse tree produced by PromQLParser#function_.
    def enterFunction_(self, ctx: PromQLParser.Function_Context):
        pass

    # Exit a parse tree produced by PromQLParser#function_.
    def exitFunction_(self, ctx: PromQLParser.Function_Context):
        pass

    # Enter a parse tree produced by PromQLParser#parameter.
    def enterParameter(self, ctx: PromQLParser.ParameterContext):
        pass

    # Exit a parse tree produced by PromQLParser#parameter.
    def exitParameter(self, ctx: PromQLParser.ParameterContext):
        pass

    # Enter a parse tree produced by PromQLParser#parameterList.
    def enterParameterList(self, ctx: PromQLParser.ParameterListContext):
        pass

    # Exit a parse tree produced by PromQLParser#parameterList.
    def exitParameterList(self, ctx: PromQLParser.ParameterListContext):
        pass

    # Enter a parse tree produced by PromQLParser#aggregation.
    def enterAggregation(self, ctx: PromQLParser.AggregationContext):
        pass

    # Exit a parse tree produced by PromQLParser#aggregation.
    def exitAggregation(self, ctx: PromQLParser.AggregationContext):
        pass

    # Enter a parse tree produced by PromQLParser#by.
    def enterBy(self, ctx: PromQLParser.ByContext):
        pass

    # Exit a parse tree produced by PromQLParser#by.
    def exitBy(self, ctx: PromQLParser.ByContext):
        pass

    # Enter a parse tree produced by PromQLParser#without.
    def enterWithout(self, ctx: PromQLParser.WithoutContext):
        pass

    # Exit a parse tree produced by PromQLParser#without.
    def exitWithout(self, ctx: PromQLParser.WithoutContext):
        pass

    # Enter a parse tree produced by PromQLParser#byWithout.
    def enterByWithout(self, ctx: PromQLParser.ByWithoutContext):
        pass

    # Exit a parse tree produced by PromQLParser#byWithout.
    def exitByWithout(self, ctx: PromQLParser.ByWithoutContext):
        pass

    # Enter a parse tree produced by PromQLParser#grouping.
    def enterGrouping(self, ctx: PromQLParser.GroupingContext):
        pass

    # Exit a parse tree produced by PromQLParser#grouping.
    def exitGrouping(self, ctx: PromQLParser.GroupingContext):
        pass

    # Enter a parse tree produced by PromQLParser#on_.
    def enterOn_(self, ctx: PromQLParser.On_Context):
        pass

    # Exit a parse tree produced by PromQLParser#on_.
    def exitOn_(self, ctx: PromQLParser.On_Context):
        pass

    # Enter a parse tree produced by PromQLParser#ignoring.
    def enterIgnoring(self, ctx: PromQLParser.IgnoringContext):
        pass

    # Exit a parse tree produced by PromQLParser#ignoring.
    def exitIgnoring(self, ctx: PromQLParser.IgnoringContext):
        pass

    # Enter a parse tree produced by PromQLParser#groupLeft.
    def enterGroupLeft(self, ctx: PromQLParser.GroupLeftContext):
        pass

    # Exit a parse tree produced by PromQLParser#groupLeft.
    def exitGroupLeft(self, ctx: PromQLParser.GroupLeftContext):
        pass

    # Enter a parse tree produced by PromQLParser#groupRight.
    def enterGroupRight(self, ctx: PromQLParser.GroupRightContext):
        pass

    # Exit a parse tree produced by PromQLParser#groupRight.
    def exitGroupRight(self, ctx: PromQLParser.GroupRightContext):
        pass

    # Enter a parse tree produced by PromQLParser#labelName.
    def enterLabelName(self, ctx: PromQLParser.LabelNameContext):
        pass

    # Exit a parse tree produced by PromQLParser#labelName.
    def exitLabelName(self, ctx: PromQLParser.LabelNameContext):
        pass

    # Enter a parse tree produced by PromQLParser#labelNameList.
    def enterLabelNameList(self, ctx: PromQLParser.LabelNameListContext):
        pass

    # Exit a parse tree produced by PromQLParser#labelNameList.
    def exitLabelNameList(self, ctx: PromQLParser.LabelNameListContext):
        pass

    # Enter a parse tree produced by PromQLParser#keyword.
    def enterKeyword(self, ctx: PromQLParser.KeywordContext):
        pass

    # Exit a parse tree produced by PromQLParser#keyword.
    def exitKeyword(self, ctx: PromQLParser.KeywordContext):
        pass

    # Enter a parse tree produced by PromQLParser#literal.
    def enterLiteral(self, ctx: PromQLParser.LiteralContext):
        pass

    # Exit a parse tree produced by PromQLParser#literal.
    def exitLiteral(self, ctx: PromQLParser.LiteralContext):
        pass


del PromQLParser
