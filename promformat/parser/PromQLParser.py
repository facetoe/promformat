# Generated from PromQLParser.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3-")
        buf.write("\u0132\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write('\4\37\t\37\4 \t \4!\t!\4"\t"\4#\t#\4$\t$\3\2\3\2\3\2')
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3Q\n\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3q\n\3\f")
        buf.write("\3\16\3t\13\3\3\4\3\4\3\5\3\5\5\5z\n\5\3\6\3\6\5\6~\n")
        buf.write("\6\3\7\3\7\5\7\u0082\n\7\3\b\3\b\5\b\u0086\n\b\3\b\5\b")
        buf.write("\u0089\n\b\3\t\3\t\5\t\u008d\n\t\3\n\3\n\5\n\u0091\n\n")
        buf.write("\3\13\3\13\5\13\u0095\n\13\3\f\3\f\5\f\u0099\n\f\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00a5\n")
        buf.write("\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\5\20\u00ae\n\20")
        buf.write("\3\20\5\20\u00b1\n\20\3\20\3\20\3\20\3\20\5\20\u00b7\n")
        buf.write("\20\3\21\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\23\7\23")
        buf.write("\u00c2\n\23\f\23\16\23\u00c5\13\23\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00d2\n\25\3")
        buf.write("\26\3\26\3\26\3\26\3\26\7\26\u00d9\n\26\f\26\16\26\u00dc")
        buf.write("\13\26\3\26\3\26\3\27\3\27\5\27\u00e2\n\27\3\30\3\30\3")
        buf.write("\30\3\30\7\30\u00e8\n\30\f\30\16\30\u00eb\13\30\5\30\u00ed")
        buf.write("\n\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\5\31\u00f6\n")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u00fe\n\31\5\31")
        buf.write("\u0100\n\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\5")
        buf.write("\34\u010a\n\34\3\34\3\34\5\34\u010e\n\34\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\5!\u011f")
        buf.write('\n!\3"\3"\3"\3"\7"\u0125\n"\f"\16"\u0128\13"')
        buf.write('\5"\u012a\n"\3"\3"\3#\3#\3$\3$\3$\2\3\4%\2\4\6\b\n')
        buf.write('\f\16\20\22\24\26\30\32\34\36 "$&(*,.\60\62\64\668:<')
        buf.write(">@BDF\2\n\3\2\5\6\3\2\7\t\3\2\17\24\4\2\13\13\r\r\4\2")
        buf.write("\r\r\31\31\5\2\16\16\20\20\25\26\4\2\13\r\27 \3\2\3\4")
        buf.write("\2\u013a\2H\3\2\2\2\4P\3\2\2\2\6u\3\2\2\2\bw\3\2\2\2\n")
        buf.write("{\3\2\2\2\f\177\3\2\2\2\16\u0083\3\2\2\2\20\u008a\3\2")
        buf.write("\2\2\22\u008e\3\2\2\2\24\u0092\3\2\2\2\26\u0096\3\2\2")
        buf.write("\2\30\u009a\3\2\2\2\32\u00a4\3\2\2\2\34\u00a6\3\2\2\2")
        buf.write('\36\u00b6\3\2\2\2 \u00b8\3\2\2\2"\u00bc\3\2\2\2$\u00be')
        buf.write("\3\2\2\2&\u00c6\3\2\2\2(\u00d1\3\2\2\2*\u00d3\3\2\2\2")
        buf.write(",\u00e1\3\2\2\2.\u00e3\3\2\2\2\60\u00ff\3\2\2\2\62\u0101")
        buf.write("\3\2\2\2\64\u0104\3\2\2\2\66\u0109\3\2\2\28\u010f\3\2")
        buf.write("\2\2:\u0112\3\2\2\2<\u0115\3\2\2\2>\u0118\3\2\2\2@\u011e")
        buf.write("\3\2\2\2B\u0120\3\2\2\2D\u012d\3\2\2\2F\u012f\3\2\2\2")
        buf.write("HI\5\4\3\2IJ\7\2\2\3J\3\3\2\2\2KL\b\3\1\2LM\5\6\4\2MN")
        buf.write("\5\4\3\nNQ\3\2\2\2OQ\5\32\16\2PK\3\2\2\2PO\3\2\2\2Qr\3")
        buf.write("\2\2\2RS\f\f\2\2ST\5\b\5\2TU\5\4\3\fUq\3\2\2\2VW\f\t\2")
        buf.write("\2WX\5\n\6\2XY\5\4\3\nYq\3\2\2\2Z[\f\b\2\2[\\\5\f\7\2")
        buf.write("\\]\5\4\3\t]q\3\2\2\2^_\f\7\2\2_`\5\16\b\2`a\5\4\3\ba")
        buf.write("q\3\2\2\2bc\f\6\2\2cd\5\20\t\2de\5\4\3\7eq\3\2\2\2fg\f")
        buf.write("\5\2\2gh\5\22\n\2hi\5\4\3\6iq\3\2\2\2jk\f\4\2\2kl\5\24")
        buf.write("\13\2lm\5\4\3\5mq\3\2\2\2no\f\13\2\2oq\5\26\f\2pR\3\2")
        buf.write("\2\2pV\3\2\2\2pZ\3\2\2\2p^\3\2\2\2pb\3\2\2\2pf\3\2\2\2")
        buf.write("pj\3\2\2\2pn\3\2\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2s\5")
        buf.write("\3\2\2\2tr\3\2\2\2uv\t\2\2\2v\7\3\2\2\2wy\7\n\2\2xz\5")
        buf.write("\66\34\2yx\3\2\2\2yz\3\2\2\2z\t\3\2\2\2{}\t\3\2\2|~\5")
        buf.write("\66\34\2}|\3\2\2\2}~\3\2\2\2~\13\3\2\2\2\177\u0081\t\2")
        buf.write("\2\2\u0080\u0082\5\66\34\2\u0081\u0080\3\2\2\2\u0081\u0082")
        buf.write("\3\2\2\2\u0082\r\3\2\2\2\u0083\u0085\t\4\2\2\u0084\u0086")
        buf.write("\7\36\2\2\u0085\u0084\3\2\2\2\u0085\u0086\3\2\2\2\u0086")
        buf.write("\u0088\3\2\2\2\u0087\u0089\5\66\34\2\u0088\u0087\3\2\2")
        buf.write("\2\u0088\u0089\3\2\2\2\u0089\17\3\2\2\2\u008a\u008c\t")
        buf.write("\5\2\2\u008b\u008d\5\66\34\2\u008c\u008b\3\2\2\2\u008c")
        buf.write("\u008d\3\2\2\2\u008d\21\3\2\2\2\u008e\u0090\7\f\2\2\u008f")
        buf.write("\u0091\5\66\34\2\u0090\u008f\3\2\2\2\u0090\u0091\3\2\2")
        buf.write("\2\u0091\23\3\2\2\2\u0092\u0094\t\6\2\2\u0093\u0095\5")
        buf.write("\66\34\2\u0094\u0093\3\2\2\2\u0094\u0095\3\2\2\2\u0095")
        buf.write("\25\3\2\2\2\u0096\u0098\7(\2\2\u0097\u0099\5\30\r\2\u0098")
        buf.write("\u0097\3\2\2\2\u0098\u0099\3\2\2\2\u0099\27\3\2\2\2\u009a")
        buf.write("\u009b\7\35\2\2\u009b\u009c\7*\2\2\u009c\31\3\2\2\2\u009d")
        buf.write("\u00a5\5*\26\2\u009e\u00a5\5\60\31\2\u009f\u00a5\5\36")
        buf.write("\20\2\u00a0\u00a5\5&\24\2\u00a1\u00a5\5(\25\2\u00a2\u00a5")
        buf.write("\5F$\2\u00a3\u00a5\5\34\17\2\u00a4\u009d\3\2\2\2\u00a4")
        buf.write("\u009e\3\2\2\2\u00a4\u009f\3\2\2\2\u00a4\u00a0\3\2\2\2")
        buf.write("\u00a4\u00a1\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a3\3")
        buf.write("\2\2\2\u00a5\33\3\2\2\2\u00a6\u00a7\7#\2\2\u00a7\u00a8")
        buf.write("\5\4\3\2\u00a8\u00a9\7$\2\2\u00a9\35\3\2\2\2\u00aa\u00b0")
        buf.write("\7+\2\2\u00ab\u00ad\7!\2\2\u00ac\u00ae\5$\23\2\u00ad\u00ac")
        buf.write("\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\3\2\2\2\u00af")
        buf.write('\u00b1\7"\2\2\u00b0\u00ab\3\2\2\2\u00b0\u00b1\3\2\2\2')
        buf.write("\u00b1\u00b7\3\2\2\2\u00b2\u00b3\7!\2\2\u00b3\u00b4\5")
        buf.write('$\23\2\u00b4\u00b5\7"\2\2\u00b5\u00b7\3\2\2\2\u00b6\u00aa')
        buf.write("\3\2\2\2\u00b6\u00b2\3\2\2\2\u00b7\37\3\2\2\2\u00b8\u00b9")
        buf.write('\5@!\2\u00b9\u00ba\5"\22\2\u00ba\u00bb\7\4\2\2\u00bb')
        buf.write("!\3\2\2\2\u00bc\u00bd\t\7\2\2\u00bd#\3\2\2\2\u00be\u00c3")
        buf.write("\5 \21\2\u00bf\u00c0\7'\2\2\u00c0\u00c2\5 \21\2\u00c1")
        buf.write("\u00bf\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c1\3\2\2\2")
        buf.write("\u00c3\u00c4\3\2\2\2\u00c4%\3\2\2\2\u00c5\u00c3\3\2\2")
        buf.write("\2\u00c6\u00c7\5\36\20\2\u00c7\u00c8\7)\2\2\u00c8'\3")
        buf.write("\2\2\2\u00c9\u00ca\5\36\20\2\u00ca\u00cb\7\35\2\2\u00cb")
        buf.write("\u00cc\7*\2\2\u00cc\u00d2\3\2\2\2\u00cd\u00ce\5&\24\2")
        buf.write("\u00ce\u00cf\7\35\2\2\u00cf\u00d0\7*\2\2\u00d0\u00d2\3")
        buf.write("\2\2\2\u00d1\u00c9\3\2\2\2\u00d1\u00cd\3\2\2\2\u00d2)")
        buf.write("\3\2\2\2\u00d3\u00d4\7 \2\2\u00d4\u00d5\7#\2\2\u00d5\u00da")
        buf.write("\5,\27\2\u00d6\u00d7\7'\2\2\u00d7\u00d9\5,\27\2\u00d8")
        buf.write("\u00d6\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2")
        buf.write("\u00da\u00db\3\2\2\2\u00db\u00dd\3\2\2\2\u00dc\u00da\3")
        buf.write("\2\2\2\u00dd\u00de\7$\2\2\u00de+\3\2\2\2\u00df\u00e2\5")
        buf.write("F$\2\u00e0\u00e2\5\4\3\2\u00e1\u00df\3\2\2\2\u00e1\u00e0")
        buf.write("\3\2\2\2\u00e2-\3\2\2\2\u00e3\u00ec\7#\2\2\u00e4\u00e9")
        buf.write("\5,\27\2\u00e5\u00e6\7'\2\2\u00e6\u00e8\5,\27\2\u00e7")
        buf.write("\u00e5\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3\2\2\2")
        buf.write("\u00e9\u00ea\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3")
        buf.write("\2\2\2\u00ec\u00e4\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ee")
        buf.write("\3\2\2\2\u00ee\u00ef\7$\2\2\u00ef/\3\2\2\2\u00f0\u00f1")
        buf.write("\7\37\2\2\u00f1\u0100\5.\30\2\u00f2\u00f5\7\37\2\2\u00f3")
        buf.write("\u00f6\5\62\32\2\u00f4\u00f6\5\64\33\2\u00f5\u00f3\3\2")
        buf.write("\2\2\u00f5\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f8")
        buf.write("\5.\30\2\u00f8\u0100\3\2\2\2\u00f9\u00fa\7\37\2\2\u00fa")
        buf.write("\u00fd\5.\30\2\u00fb\u00fe\5\62\32\2\u00fc\u00fe\5\64")
        buf.write("\33\2\u00fd\u00fb\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe\u0100")
        buf.write("\3\2\2\2\u00ff\u00f0\3\2\2\2\u00ff\u00f2\3\2\2\2\u00ff")
        buf.write("\u00f9\3\2\2\2\u0100\61\3\2\2\2\u0101\u0102\7\27\2\2\u0102")
        buf.write('\u0103\5B"\2\u0103\63\3\2\2\2\u0104\u0105\7\30\2\2\u0105')
        buf.write('\u0106\5B"\2\u0106\65\3\2\2\2\u0107\u010a\58\35\2\u0108')
        buf.write("\u010a\5:\36\2\u0109\u0107\3\2\2\2\u0109\u0108\3\2\2\2")
        buf.write("\u010a\u010d\3\2\2\2\u010b\u010e\5<\37\2\u010c\u010e\5")
        buf.write("> \2\u010d\u010b\3\2\2\2\u010d\u010c\3\2\2\2\u010d\u010e")
        buf.write("\3\2\2\2\u010e\67\3\2\2\2\u010f\u0110\7\31\2\2\u0110\u0111")
        buf.write('\5B"\2\u01119\3\2\2\2\u0112\u0113\7\32\2\2\u0113\u0114')
        buf.write('\5B"\2\u0114;\3\2\2\2\u0115\u0116\7\33\2\2\u0116\u0117')
        buf.write('\5B"\2\u0117=\3\2\2\2\u0118\u0119\7\34\2\2\u0119\u011a')
        buf.write('\5B"\2\u011a?\3\2\2\2\u011b\u011f\5D#\2\u011c\u011f\7')
        buf.write("+\2\2\u011d\u011f\7,\2\2\u011e\u011b\3\2\2\2\u011e\u011c")
        buf.write("\3\2\2\2\u011e\u011d\3\2\2\2\u011fA\3\2\2\2\u0120\u0129")
        buf.write("\7#\2\2\u0121\u0126\5@!\2\u0122\u0123\7'\2\2\u0123\u0125")
        buf.write("\5@!\2\u0124\u0122\3\2\2\2\u0125\u0128\3\2\2\2\u0126\u0124")
        buf.write("\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u012a\3\2\2\2\u0128")
        buf.write("\u0126\3\2\2\2\u0129\u0121\3\2\2\2\u0129\u012a\3\2\2\2")
        buf.write("\u012a\u012b\3\2\2\2\u012b\u012c\7$\2\2\u012cC\3\2\2\2")
        buf.write("\u012d\u012e\t\b\2\2\u012eE\3\2\2\2\u012f\u0130\t\t\2")
        buf.write("\2\u0130G\3\2\2\2 Ppry}\u0081\u0085\u0088\u008c\u0090")
        buf.write("\u0094\u0098\u00a4\u00ad\u00b0\u00b6\u00c3\u00d1\u00da")
        buf.write("\u00e1\u00e9\u00ec\u00f5\u00fd\u00ff\u0109\u010d\u011e")
        buf.write("\u0126\u0129")
        return buf.getvalue()


class PromQLParser(Parser):

    grammarFileName = "PromQLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = [
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "'+'",
        "'-'",
        "'*'",
        "'/'",
        "'%'",
        "'^'",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "'='",
        "'=='",
        "'!='",
        "'>'",
        "'<'",
        "'>='",
        "'<='",
        "'=~'",
        "'!~'",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "'{'",
        "'}'",
        "'('",
        "')'",
        "'['",
        "']'",
        "','",
    ]

    symbolicNames = [
        "<INVALID>",
        "NUMBER",
        "STRING",
        "ADD",
        "SUB",
        "MULT",
        "DIV",
        "MOD",
        "POW",
        "AND",
        "OR",
        "UNLESS",
        "EQ",
        "DEQ",
        "NE",
        "GT",
        "LT",
        "GE",
        "LE",
        "RE",
        "NRE",
        "BY",
        "WITHOUT",
        "ON",
        "IGNORING",
        "GROUP_LEFT",
        "GROUP_RIGHT",
        "OFFSET",
        "BOOL",
        "AGGREGATION_OPERATOR",
        "FUNCTION",
        "LEFT_BRACE",
        "RIGHT_BRACE",
        "LEFT_PAREN",
        "RIGHT_PAREN",
        "LEFT_BRACKET",
        "RIGHT_BRACKET",
        "COMMA",
        "SUBQUERY_RANGE",
        "TIME_RANGE",
        "DURATION",
        "METRIC_NAME",
        "LABEL_NAME",
        "WS",
    ]

    RULE_expression = 0
    RULE_vectorOperation = 1
    RULE_unaryOp = 2
    RULE_powOp = 3
    RULE_multOp = 4
    RULE_addOp = 5
    RULE_compareOp = 6
    RULE_andUnlessOp = 7
    RULE_orOp = 8
    RULE_vectorMatchOp = 9
    RULE_subqueryOp = 10
    RULE_offsetOp = 11
    RULE_vector = 12
    RULE_parens = 13
    RULE_instantSelector = 14
    RULE_labelMatcher = 15
    RULE_labelMatcherOperator = 16
    RULE_labelMatcherList = 17
    RULE_matrixSelector = 18
    RULE_offset = 19
    RULE_function_ = 20
    RULE_parameter = 21
    RULE_parameterList = 22
    RULE_aggregation = 23
    RULE_by = 24
    RULE_without = 25
    RULE_grouping = 26
    RULE_on_ = 27
    RULE_ignoring = 28
    RULE_groupLeft = 29
    RULE_groupRight = 30
    RULE_labelName = 31
    RULE_labelNameList = 32
    RULE_keyword = 33
    RULE_literal = 34

    ruleNames = [
        "expression",
        "vectorOperation",
        "unaryOp",
        "powOp",
        "multOp",
        "addOp",
        "compareOp",
        "andUnlessOp",
        "orOp",
        "vectorMatchOp",
        "subqueryOp",
        "offsetOp",
        "vector",
        "parens",
        "instantSelector",
        "labelMatcher",
        "labelMatcherOperator",
        "labelMatcherList",
        "matrixSelector",
        "offset",
        "function_",
        "parameter",
        "parameterList",
        "aggregation",
        "by",
        "without",
        "grouping",
        "on_",
        "ignoring",
        "groupLeft",
        "groupRight",
        "labelName",
        "labelNameList",
        "keyword",
        "literal",
    ]

    EOF = Token.EOF
    NUMBER = 1
    STRING = 2
    ADD = 3
    SUB = 4
    MULT = 5
    DIV = 6
    MOD = 7
    POW = 8
    AND = 9
    OR = 10
    UNLESS = 11
    EQ = 12
    DEQ = 13
    NE = 14
    GT = 15
    LT = 16
    GE = 17
    LE = 18
    RE = 19
    NRE = 20
    BY = 21
    WITHOUT = 22
    ON = 23
    IGNORING = 24
    GROUP_LEFT = 25
    GROUP_RIGHT = 26
    OFFSET = 27
    BOOL = 28
    AGGREGATION_OPERATOR = 29
    FUNCTION = 30
    LEFT_BRACE = 31
    RIGHT_BRACE = 32
    LEFT_PAREN = 33
    RIGHT_PAREN = 34
    LEFT_BRACKET = 35
    RIGHT_BRACKET = 36
    COMMA = 37
    SUBQUERY_RANGE = 38
    TIME_RANGE = 39
    DURATION = 40
    METRIC_NAME = 41
    LABEL_NAME = 42
    WS = 43

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class ExpressionContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vectorOperation(self):
            return self.getTypedRuleContext(PromQLParser.VectorOperationContext, 0)

        def EOF(self):
            return self.getToken(PromQLParser.EOF, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_expression

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterExpression"):
                listener.enterExpression(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitExpression"):
                listener.exitExpression(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitExpression"):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)

    def expression(self):

        localctx = PromQLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.vectorOperation(0)
            self.state = 71
            self.match(PromQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VectorOperationContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryOp(self):
            return self.getTypedRuleContext(PromQLParser.UnaryOpContext, 0)

        def vectorOperation(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PromQLParser.VectorOperationContext)
            else:
                return self.getTypedRuleContext(PromQLParser.VectorOperationContext, i)

        def vector(self):
            return self.getTypedRuleContext(PromQLParser.VectorContext, 0)

        def powOp(self):
            return self.getTypedRuleContext(PromQLParser.PowOpContext, 0)

        def multOp(self):
            return self.getTypedRuleContext(PromQLParser.MultOpContext, 0)

        def addOp(self):
            return self.getTypedRuleContext(PromQLParser.AddOpContext, 0)

        def compareOp(self):
            return self.getTypedRuleContext(PromQLParser.CompareOpContext, 0)

        def andUnlessOp(self):
            return self.getTypedRuleContext(PromQLParser.AndUnlessOpContext, 0)

        def orOp(self):
            return self.getTypedRuleContext(PromQLParser.OrOpContext, 0)

        def vectorMatchOp(self):
            return self.getTypedRuleContext(PromQLParser.VectorMatchOpContext, 0)

        def subqueryOp(self):
            return self.getTypedRuleContext(PromQLParser.SubqueryOpContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_vectorOperation

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVectorOperation"):
                listener.enterVectorOperation(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVectorOperation"):
                listener.exitVectorOperation(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitVectorOperation"):
                return visitor.visitVectorOperation(self)
            else:
                return visitor.visitChildren(self)

    def vectorOperation(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PromQLParser.VectorOperationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_vectorOperation, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PromQLParser.ADD, PromQLParser.SUB]:
                self.state = 74
                self.unaryOp()
                self.state = 75
                self.vectorOperation(8)
                pass
            elif token in [
                PromQLParser.NUMBER,
                PromQLParser.STRING,
                PromQLParser.AGGREGATION_OPERATOR,
                PromQLParser.FUNCTION,
                PromQLParser.LEFT_BRACE,
                PromQLParser.LEFT_PAREN,
                PromQLParser.METRIC_NAME,
            ]:
                self.state = 77
                self.vector()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 110
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 1, self._ctx)
                    if la_ == 1:
                        localctx = PromQLParser.VectorOperationContext(
                            self, _parentctx, _parentState
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_vectorOperation
                        )
                        self.state = 80
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 10)"
                            )
                        self.state = 81
                        self.powOp()
                        self.state = 82
                        self.vectorOperation(10)
                        pass

                    elif la_ == 2:
                        localctx = PromQLParser.VectorOperationContext(
                            self, _parentctx, _parentState
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_vectorOperation
                        )
                        self.state = 84
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 7)"
                            )
                        self.state = 85
                        self.multOp()
                        self.state = 86
                        self.vectorOperation(8)
                        pass

                    elif la_ == 3:
                        localctx = PromQLParser.VectorOperationContext(
                            self, _parentctx, _parentState
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_vectorOperation
                        )
                        self.state = 88
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 6)"
                            )
                        self.state = 89
                        self.addOp()
                        self.state = 90
                        self.vectorOperation(7)
                        pass

                    elif la_ == 4:
                        localctx = PromQLParser.VectorOperationContext(
                            self, _parentctx, _parentState
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_vectorOperation
                        )
                        self.state = 92
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 5)"
                            )
                        self.state = 93
                        self.compareOp()
                        self.state = 94
                        self.vectorOperation(6)
                        pass

                    elif la_ == 5:
                        localctx = PromQLParser.VectorOperationContext(
                            self, _parentctx, _parentState
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_vectorOperation
                        )
                        self.state = 96
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 4)"
                            )
                        self.state = 97
                        self.andUnlessOp()
                        self.state = 98
                        self.vectorOperation(5)
                        pass

                    elif la_ == 6:
                        localctx = PromQLParser.VectorOperationContext(
                            self, _parentctx, _parentState
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_vectorOperation
                        )
                        self.state = 100
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 3)"
                            )
                        self.state = 101
                        self.orOp()
                        self.state = 102
                        self.vectorOperation(4)
                        pass

                    elif la_ == 7:
                        localctx = PromQLParser.VectorOperationContext(
                            self, _parentctx, _parentState
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_vectorOperation
                        )
                        self.state = 104
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 2)"
                            )
                        self.state = 105
                        self.vectorMatchOp()
                        self.state = 106
                        self.vectorOperation(3)
                        pass

                    elif la_ == 8:
                        localctx = PromQLParser.VectorOperationContext(
                            self, _parentctx, _parentState
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_vectorOperation
                        )
                        self.state = 108
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 9)"
                            )
                        self.state = 109
                        self.subqueryOp()
                        pass

                self.state = 114
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class UnaryOpContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(PromQLParser.ADD, 0)

        def SUB(self):
            return self.getToken(PromQLParser.SUB, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_unaryOp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterUnaryOp"):
                listener.enterUnaryOp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitUnaryOp"):
                listener.exitUnaryOp(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitUnaryOp"):
                return visitor.visitUnaryOp(self)
            else:
                return visitor.visitChildren(self)

    def unaryOp(self):

        localctx = PromQLParser.UnaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_unaryOp)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            _la = self._input.LA(1)
            if not (_la == PromQLParser.ADD or _la == PromQLParser.SUB):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PowOpContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POW(self):
            return self.getToken(PromQLParser.POW, 0)

        def grouping(self):
            return self.getTypedRuleContext(PromQLParser.GroupingContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_powOp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPowOp"):
                listener.enterPowOp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPowOp"):
                listener.exitPowOp(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPowOp"):
                return visitor.visitPowOp(self)
            else:
                return visitor.visitChildren(self)

    def powOp(self):

        localctx = PromQLParser.PowOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_powOp)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(PromQLParser.POW)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == PromQLParser.ON or _la == PromQLParser.IGNORING:
                self.state = 118
                self.grouping()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MultOpContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(PromQLParser.MULT, 0)

        def DIV(self):
            return self.getToken(PromQLParser.DIV, 0)

        def MOD(self):
            return self.getToken(PromQLParser.MOD, 0)

        def grouping(self):
            return self.getTypedRuleContext(PromQLParser.GroupingContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_multOp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterMultOp"):
                listener.enterMultOp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitMultOp"):
                listener.exitMultOp(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMultOp"):
                return visitor.visitMultOp(self)
            else:
                return visitor.visitChildren(self)

    def multOp(self):

        localctx = PromQLParser.MultOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_multOp)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            _la = self._input.LA(1)
            if not (
                (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << PromQLParser.MULT)
                            | (1 << PromQLParser.DIV)
                            | (1 << PromQLParser.MOD)
                        )
                    )
                    != 0
                )
            ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == PromQLParser.ON or _la == PromQLParser.IGNORING:
                self.state = 122
                self.grouping()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AddOpContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(PromQLParser.ADD, 0)

        def SUB(self):
            return self.getToken(PromQLParser.SUB, 0)

        def grouping(self):
            return self.getTypedRuleContext(PromQLParser.GroupingContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_addOp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAddOp"):
                listener.enterAddOp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAddOp"):
                listener.exitAddOp(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAddOp"):
                return visitor.visitAddOp(self)
            else:
                return visitor.visitChildren(self)

    def addOp(self):

        localctx = PromQLParser.AddOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_addOp)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            _la = self._input.LA(1)
            if not (_la == PromQLParser.ADD or _la == PromQLParser.SUB):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == PromQLParser.ON or _la == PromQLParser.IGNORING:
                self.state = 126
                self.grouping()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompareOpContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEQ(self):
            return self.getToken(PromQLParser.DEQ, 0)

        def NE(self):
            return self.getToken(PromQLParser.NE, 0)

        def GT(self):
            return self.getToken(PromQLParser.GT, 0)

        def LT(self):
            return self.getToken(PromQLParser.LT, 0)

        def GE(self):
            return self.getToken(PromQLParser.GE, 0)

        def LE(self):
            return self.getToken(PromQLParser.LE, 0)

        def BOOL(self):
            return self.getToken(PromQLParser.BOOL, 0)

        def grouping(self):
            return self.getTypedRuleContext(PromQLParser.GroupingContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_compareOp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterCompareOp"):
                listener.enterCompareOp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitCompareOp"):
                listener.exitCompareOp(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitCompareOp"):
                return visitor.visitCompareOp(self)
            else:
                return visitor.visitChildren(self)

    def compareOp(self):

        localctx = PromQLParser.CompareOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_compareOp)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            _la = self._input.LA(1)
            if not (
                (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << PromQLParser.DEQ)
                            | (1 << PromQLParser.NE)
                            | (1 << PromQLParser.GT)
                            | (1 << PromQLParser.LT)
                            | (1 << PromQLParser.GE)
                            | (1 << PromQLParser.LE)
                        )
                    )
                    != 0
                )
            ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == PromQLParser.BOOL:
                self.state = 130
                self.match(PromQLParser.BOOL)

            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == PromQLParser.ON or _la == PromQLParser.IGNORING:
                self.state = 133
                self.grouping()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AndUnlessOpContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(PromQLParser.AND, 0)

        def UNLESS(self):
            return self.getToken(PromQLParser.UNLESS, 0)

        def grouping(self):
            return self.getTypedRuleContext(PromQLParser.GroupingContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_andUnlessOp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAndUnlessOp"):
                listener.enterAndUnlessOp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAndUnlessOp"):
                listener.exitAndUnlessOp(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAndUnlessOp"):
                return visitor.visitAndUnlessOp(self)
            else:
                return visitor.visitChildren(self)

    def andUnlessOp(self):

        localctx = PromQLParser.AndUnlessOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_andUnlessOp)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            _la = self._input.LA(1)
            if not (_la == PromQLParser.AND or _la == PromQLParser.UNLESS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == PromQLParser.ON or _la == PromQLParser.IGNORING:
                self.state = 137
                self.grouping()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OrOpContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(PromQLParser.OR, 0)

        def grouping(self):
            return self.getTypedRuleContext(PromQLParser.GroupingContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_orOp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterOrOp"):
                listener.enterOrOp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitOrOp"):
                listener.exitOrOp(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitOrOp"):
                return visitor.visitOrOp(self)
            else:
                return visitor.visitChildren(self)

    def orOp(self):

        localctx = PromQLParser.OrOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_orOp)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(PromQLParser.OR)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == PromQLParser.ON or _la == PromQLParser.IGNORING:
                self.state = 141
                self.grouping()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VectorMatchOpContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ON(self):
            return self.getToken(PromQLParser.ON, 0)

        def UNLESS(self):
            return self.getToken(PromQLParser.UNLESS, 0)

        def grouping(self):
            return self.getTypedRuleContext(PromQLParser.GroupingContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_vectorMatchOp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVectorMatchOp"):
                listener.enterVectorMatchOp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVectorMatchOp"):
                listener.exitVectorMatchOp(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitVectorMatchOp"):
                return visitor.visitVectorMatchOp(self)
            else:
                return visitor.visitChildren(self)

    def vectorMatchOp(self):

        localctx = PromQLParser.VectorMatchOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_vectorMatchOp)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not (_la == PromQLParser.UNLESS or _la == PromQLParser.ON):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == PromQLParser.ON or _la == PromQLParser.IGNORING:
                self.state = 145
                self.grouping()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubqueryOpContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBQUERY_RANGE(self):
            return self.getToken(PromQLParser.SUBQUERY_RANGE, 0)

        def offsetOp(self):
            return self.getTypedRuleContext(PromQLParser.OffsetOpContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_subqueryOp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSubqueryOp"):
                listener.enterSubqueryOp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSubqueryOp"):
                listener.exitSubqueryOp(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSubqueryOp"):
                return visitor.visitSubqueryOp(self)
            else:
                return visitor.visitChildren(self)

    def subqueryOp(self):

        localctx = PromQLParser.SubqueryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_subqueryOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(PromQLParser.SUBQUERY_RANGE)
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 11, self._ctx)
            if la_ == 1:
                self.state = 149
                self.offsetOp()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OffsetOpContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OFFSET(self):
            return self.getToken(PromQLParser.OFFSET, 0)

        def DURATION(self):
            return self.getToken(PromQLParser.DURATION, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_offsetOp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterOffsetOp"):
                listener.enterOffsetOp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitOffsetOp"):
                listener.exitOffsetOp(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitOffsetOp"):
                return visitor.visitOffsetOp(self)
            else:
                return visitor.visitChildren(self)

    def offsetOp(self):

        localctx = PromQLParser.OffsetOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_offsetOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(PromQLParser.OFFSET)
            self.state = 153
            self.match(PromQLParser.DURATION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VectorContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_(self):
            return self.getTypedRuleContext(PromQLParser.Function_Context, 0)

        def aggregation(self):
            return self.getTypedRuleContext(PromQLParser.AggregationContext, 0)

        def instantSelector(self):
            return self.getTypedRuleContext(PromQLParser.InstantSelectorContext, 0)

        def matrixSelector(self):
            return self.getTypedRuleContext(PromQLParser.MatrixSelectorContext, 0)

        def offset(self):
            return self.getTypedRuleContext(PromQLParser.OffsetContext, 0)

        def literal(self):
            return self.getTypedRuleContext(PromQLParser.LiteralContext, 0)

        def parens(self):
            return self.getTypedRuleContext(PromQLParser.ParensContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_vector

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVector"):
                listener.enterVector(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVector"):
                listener.exitVector(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitVector"):
                return visitor.visitVector(self)
            else:
                return visitor.visitChildren(self)

    def vector(self):

        localctx = PromQLParser.VectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_vector)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 12, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.function_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.aggregation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.instantSelector()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 158
                self.matrixSelector()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 159
                self.offset()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 160
                self.literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 161
                self.parens()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParensContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(PromQLParser.LEFT_PAREN, 0)

        def vectorOperation(self):
            return self.getTypedRuleContext(PromQLParser.VectorOperationContext, 0)

        def RIGHT_PAREN(self):
            return self.getToken(PromQLParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_parens

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterParens"):
                listener.enterParens(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitParens"):
                listener.exitParens(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitParens"):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)

    def parens(self):

        localctx = PromQLParser.ParensContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parens)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(PromQLParser.LEFT_PAREN)
            self.state = 165
            self.vectorOperation(0)
            self.state = 166
            self.match(PromQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InstantSelectorContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def METRIC_NAME(self):
            return self.getToken(PromQLParser.METRIC_NAME, 0)

        def LEFT_BRACE(self):
            return self.getToken(PromQLParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(PromQLParser.RIGHT_BRACE, 0)

        def labelMatcherList(self):
            return self.getTypedRuleContext(PromQLParser.LabelMatcherListContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_instantSelector

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterInstantSelector"):
                listener.enterInstantSelector(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitInstantSelector"):
                listener.exitInstantSelector(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitInstantSelector"):
                return visitor.visitInstantSelector(self)
            else:
                return visitor.visitChildren(self)

    def instantSelector(self):

        localctx = PromQLParser.InstantSelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_instantSelector)
        self._la = 0  # Token type
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PromQLParser.METRIC_NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(PromQLParser.METRIC_NAME)
                self.state = 174
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 14, self._ctx)
                if la_ == 1:
                    self.state = 169
                    self.match(PromQLParser.LEFT_BRACE)
                    self.state = 171
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if ((_la) & ~0x3F) == 0 and (
                        (1 << _la)
                        & (
                            (1 << PromQLParser.AND)
                            | (1 << PromQLParser.OR)
                            | (1 << PromQLParser.UNLESS)
                            | (1 << PromQLParser.BY)
                            | (1 << PromQLParser.WITHOUT)
                            | (1 << PromQLParser.ON)
                            | (1 << PromQLParser.IGNORING)
                            | (1 << PromQLParser.GROUP_LEFT)
                            | (1 << PromQLParser.GROUP_RIGHT)
                            | (1 << PromQLParser.OFFSET)
                            | (1 << PromQLParser.BOOL)
                            | (1 << PromQLParser.AGGREGATION_OPERATOR)
                            | (1 << PromQLParser.FUNCTION)
                            | (1 << PromQLParser.METRIC_NAME)
                            | (1 << PromQLParser.LABEL_NAME)
                        )
                    ) != 0:
                        self.state = 170
                        self.labelMatcherList()

                    self.state = 173
                    self.match(PromQLParser.RIGHT_BRACE)

                pass
            elif token in [PromQLParser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.match(PromQLParser.LEFT_BRACE)
                self.state = 177
                self.labelMatcherList()
                self.state = 178
                self.match(PromQLParser.RIGHT_BRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelMatcherContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labelName(self):
            return self.getTypedRuleContext(PromQLParser.LabelNameContext, 0)

        def labelMatcherOperator(self):
            return self.getTypedRuleContext(PromQLParser.LabelMatcherOperatorContext, 0)

        def STRING(self):
            return self.getToken(PromQLParser.STRING, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_labelMatcher

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLabelMatcher"):
                listener.enterLabelMatcher(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLabelMatcher"):
                listener.exitLabelMatcher(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLabelMatcher"):
                return visitor.visitLabelMatcher(self)
            else:
                return visitor.visitChildren(self)

    def labelMatcher(self):

        localctx = PromQLParser.LabelMatcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_labelMatcher)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.labelName()
            self.state = 183
            self.labelMatcherOperator()
            self.state = 184
            self.match(PromQLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelMatcherOperatorContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(PromQLParser.EQ, 0)

        def NE(self):
            return self.getToken(PromQLParser.NE, 0)

        def RE(self):
            return self.getToken(PromQLParser.RE, 0)

        def NRE(self):
            return self.getToken(PromQLParser.NRE, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_labelMatcherOperator

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLabelMatcherOperator"):
                listener.enterLabelMatcherOperator(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLabelMatcherOperator"):
                listener.exitLabelMatcherOperator(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLabelMatcherOperator"):
                return visitor.visitLabelMatcherOperator(self)
            else:
                return visitor.visitChildren(self)

    def labelMatcherOperator(self):

        localctx = PromQLParser.LabelMatcherOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_labelMatcherOperator)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            _la = self._input.LA(1)
            if not (
                (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << PromQLParser.EQ)
                            | (1 << PromQLParser.NE)
                            | (1 << PromQLParser.RE)
                            | (1 << PromQLParser.NRE)
                        )
                    )
                    != 0
                )
            ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelMatcherListContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labelMatcher(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PromQLParser.LabelMatcherContext)
            else:
                return self.getTypedRuleContext(PromQLParser.LabelMatcherContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(PromQLParser.COMMA)
            else:
                return self.getToken(PromQLParser.COMMA, i)

        def getRuleIndex(self):
            return PromQLParser.RULE_labelMatcherList

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLabelMatcherList"):
                listener.enterLabelMatcherList(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLabelMatcherList"):
                listener.exitLabelMatcherList(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLabelMatcherList"):
                return visitor.visitLabelMatcherList(self)
            else:
                return visitor.visitChildren(self)

    def labelMatcherList(self):

        localctx = PromQLParser.LabelMatcherListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_labelMatcherList)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.labelMatcher()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == PromQLParser.COMMA:
                self.state = 189
                self.match(PromQLParser.COMMA)
                self.state = 190
                self.labelMatcher()
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MatrixSelectorContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instantSelector(self):
            return self.getTypedRuleContext(PromQLParser.InstantSelectorContext, 0)

        def TIME_RANGE(self):
            return self.getToken(PromQLParser.TIME_RANGE, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_matrixSelector

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterMatrixSelector"):
                listener.enterMatrixSelector(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitMatrixSelector"):
                listener.exitMatrixSelector(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMatrixSelector"):
                return visitor.visitMatrixSelector(self)
            else:
                return visitor.visitChildren(self)

    def matrixSelector(self):

        localctx = PromQLParser.MatrixSelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_matrixSelector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.instantSelector()
            self.state = 197
            self.match(PromQLParser.TIME_RANGE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OffsetContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instantSelector(self):
            return self.getTypedRuleContext(PromQLParser.InstantSelectorContext, 0)

        def OFFSET(self):
            return self.getToken(PromQLParser.OFFSET, 0)

        def DURATION(self):
            return self.getToken(PromQLParser.DURATION, 0)

        def matrixSelector(self):
            return self.getTypedRuleContext(PromQLParser.MatrixSelectorContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_offset

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterOffset"):
                listener.enterOffset(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitOffset"):
                listener.exitOffset(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitOffset"):
                return visitor.visitOffset(self)
            else:
                return visitor.visitChildren(self)

    def offset(self):

        localctx = PromQLParser.OffsetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_offset)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 17, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.instantSelector()
                self.state = 200
                self.match(PromQLParser.OFFSET)
                self.state = 201
                self.match(PromQLParser.DURATION)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.matrixSelector()
                self.state = 204
                self.match(PromQLParser.OFFSET)
                self.state = 205
                self.match(PromQLParser.DURATION)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_Context(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(PromQLParser.FUNCTION, 0)

        def LEFT_PAREN(self):
            return self.getToken(PromQLParser.LEFT_PAREN, 0)

        def parameter(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PromQLParser.ParameterContext)
            else:
                return self.getTypedRuleContext(PromQLParser.ParameterContext, i)

        def RIGHT_PAREN(self):
            return self.getToken(PromQLParser.RIGHT_PAREN, 0)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(PromQLParser.COMMA)
            else:
                return self.getToken(PromQLParser.COMMA, i)

        def getRuleIndex(self):
            return PromQLParser.RULE_function_

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFunction_"):
                listener.enterFunction_(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFunction_"):
                listener.exitFunction_(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFunction_"):
                return visitor.visitFunction_(self)
            else:
                return visitor.visitChildren(self)

    def function_(self):

        localctx = PromQLParser.Function_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_function_)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(PromQLParser.FUNCTION)
            self.state = 210
            self.match(PromQLParser.LEFT_PAREN)
            self.state = 211
            self.parameter()
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == PromQLParser.COMMA:
                self.state = 212
                self.match(PromQLParser.COMMA)
                self.state = 213
                self.parameter()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 219
            self.match(PromQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(PromQLParser.LiteralContext, 0)

        def vectorOperation(self):
            return self.getTypedRuleContext(PromQLParser.VectorOperationContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_parameter

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterParameter"):
                listener.enterParameter(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitParameter"):
                listener.exitParameter(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitParameter"):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)

    def parameter(self):

        localctx = PromQLParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_parameter)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 19, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.vectorOperation(0)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterListContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(PromQLParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(PromQLParser.RIGHT_PAREN, 0)

        def parameter(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PromQLParser.ParameterContext)
            else:
                return self.getTypedRuleContext(PromQLParser.ParameterContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(PromQLParser.COMMA)
            else:
                return self.getToken(PromQLParser.COMMA, i)

        def getRuleIndex(self):
            return PromQLParser.RULE_parameterList

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterParameterList"):
                listener.enterParameterList(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitParameterList"):
                listener.exitParameterList(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitParameterList"):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)

    def parameterList(self):

        localctx = PromQLParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_parameterList)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(PromQLParser.LEFT_PAREN)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3F) == 0 and (
                (1 << _la)
                & (
                    (1 << PromQLParser.NUMBER)
                    | (1 << PromQLParser.STRING)
                    | (1 << PromQLParser.ADD)
                    | (1 << PromQLParser.SUB)
                    | (1 << PromQLParser.AGGREGATION_OPERATOR)
                    | (1 << PromQLParser.FUNCTION)
                    | (1 << PromQLParser.LEFT_BRACE)
                    | (1 << PromQLParser.LEFT_PAREN)
                    | (1 << PromQLParser.METRIC_NAME)
                )
            ) != 0:
                self.state = 226
                self.parameter()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == PromQLParser.COMMA:
                    self.state = 227
                    self.match(PromQLParser.COMMA)
                    self.state = 228
                    self.parameter()
                    self.state = 233
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 236
            self.match(PromQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AggregationContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGGREGATION_OPERATOR(self):
            return self.getToken(PromQLParser.AGGREGATION_OPERATOR, 0)

        def parameterList(self):
            return self.getTypedRuleContext(PromQLParser.ParameterListContext, 0)

        def by(self):
            return self.getTypedRuleContext(PromQLParser.ByContext, 0)

        def without(self):
            return self.getTypedRuleContext(PromQLParser.WithoutContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_aggregation

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAggregation"):
                listener.enterAggregation(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAggregation"):
                listener.exitAggregation(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAggregation"):
                return visitor.visitAggregation(self)
            else:
                return visitor.visitChildren(self)

    def aggregation(self):

        localctx = PromQLParser.AggregationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_aggregation)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 24, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(PromQLParser.AGGREGATION_OPERATOR)
                self.state = 239
                self.parameterList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.match(PromQLParser.AGGREGATION_OPERATOR)
                self.state = 243
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [PromQLParser.BY]:
                    self.state = 241
                    self.by()
                    pass
                elif token in [PromQLParser.WITHOUT]:
                    self.state = 242
                    self.without()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 245
                self.parameterList()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 247
                self.match(PromQLParser.AGGREGATION_OPERATOR)
                self.state = 248
                self.parameterList()
                self.state = 251
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [PromQLParser.BY]:
                    self.state = 249
                    self.by()
                    pass
                elif token in [PromQLParser.WITHOUT]:
                    self.state = 250
                    self.without()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ByContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BY(self):
            return self.getToken(PromQLParser.BY, 0)

        def labelNameList(self):
            return self.getTypedRuleContext(PromQLParser.LabelNameListContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_by

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBy"):
                listener.enterBy(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBy"):
                listener.exitBy(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBy"):
                return visitor.visitBy(self)
            else:
                return visitor.visitChildren(self)

    def by(self):

        localctx = PromQLParser.ByContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_by)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(PromQLParser.BY)
            self.state = 256
            self.labelNameList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WithoutContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WITHOUT(self):
            return self.getToken(PromQLParser.WITHOUT, 0)

        def labelNameList(self):
            return self.getTypedRuleContext(PromQLParser.LabelNameListContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_without

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterWithout"):
                listener.enterWithout(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitWithout"):
                listener.exitWithout(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitWithout"):
                return visitor.visitWithout(self)
            else:
                return visitor.visitChildren(self)

    def without(self):

        localctx = PromQLParser.WithoutContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_without)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(PromQLParser.WITHOUT)
            self.state = 259
            self.labelNameList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroupingContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def on_(self):
            return self.getTypedRuleContext(PromQLParser.On_Context, 0)

        def ignoring(self):
            return self.getTypedRuleContext(PromQLParser.IgnoringContext, 0)

        def groupLeft(self):
            return self.getTypedRuleContext(PromQLParser.GroupLeftContext, 0)

        def groupRight(self):
            return self.getTypedRuleContext(PromQLParser.GroupRightContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_grouping

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterGrouping"):
                listener.enterGrouping(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitGrouping"):
                listener.exitGrouping(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitGrouping"):
                return visitor.visitGrouping(self)
            else:
                return visitor.visitChildren(self)

    def grouping(self):

        localctx = PromQLParser.GroupingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_grouping)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PromQLParser.ON]:
                self.state = 261
                self.on_()
                pass
            elif token in [PromQLParser.IGNORING]:
                self.state = 262
                self.ignoring()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PromQLParser.GROUP_LEFT]:
                self.state = 265
                self.groupLeft()
                pass
            elif token in [PromQLParser.GROUP_RIGHT]:
                self.state = 266
                self.groupRight()
                pass
            elif token in [
                PromQLParser.NUMBER,
                PromQLParser.STRING,
                PromQLParser.ADD,
                PromQLParser.SUB,
                PromQLParser.AGGREGATION_OPERATOR,
                PromQLParser.FUNCTION,
                PromQLParser.LEFT_BRACE,
                PromQLParser.LEFT_PAREN,
                PromQLParser.METRIC_NAME,
            ]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class On_Context(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ON(self):
            return self.getToken(PromQLParser.ON, 0)

        def labelNameList(self):
            return self.getTypedRuleContext(PromQLParser.LabelNameListContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_on_

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterOn_"):
                listener.enterOn_(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitOn_"):
                listener.exitOn_(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitOn_"):
                return visitor.visitOn_(self)
            else:
                return visitor.visitChildren(self)

    def on_(self):

        localctx = PromQLParser.On_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_on_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(PromQLParser.ON)
            self.state = 270
            self.labelNameList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IgnoringContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IGNORING(self):
            return self.getToken(PromQLParser.IGNORING, 0)

        def labelNameList(self):
            return self.getTypedRuleContext(PromQLParser.LabelNameListContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_ignoring

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterIgnoring"):
                listener.enterIgnoring(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitIgnoring"):
                listener.exitIgnoring(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIgnoring"):
                return visitor.visitIgnoring(self)
            else:
                return visitor.visitChildren(self)

    def ignoring(self):

        localctx = PromQLParser.IgnoringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_ignoring)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(PromQLParser.IGNORING)
            self.state = 273
            self.labelNameList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroupLeftContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUP_LEFT(self):
            return self.getToken(PromQLParser.GROUP_LEFT, 0)

        def labelNameList(self):
            return self.getTypedRuleContext(PromQLParser.LabelNameListContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_groupLeft

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterGroupLeft"):
                listener.enterGroupLeft(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitGroupLeft"):
                listener.exitGroupLeft(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitGroupLeft"):
                return visitor.visitGroupLeft(self)
            else:
                return visitor.visitChildren(self)

    def groupLeft(self):

        localctx = PromQLParser.GroupLeftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_groupLeft)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(PromQLParser.GROUP_LEFT)
            self.state = 276
            self.labelNameList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroupRightContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUP_RIGHT(self):
            return self.getToken(PromQLParser.GROUP_RIGHT, 0)

        def labelNameList(self):
            return self.getTypedRuleContext(PromQLParser.LabelNameListContext, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_groupRight

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterGroupRight"):
                listener.enterGroupRight(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitGroupRight"):
                listener.exitGroupRight(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitGroupRight"):
                return visitor.visitGroupRight(self)
            else:
                return visitor.visitChildren(self)

    def groupRight(self):

        localctx = PromQLParser.GroupRightContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_groupRight)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(PromQLParser.GROUP_RIGHT)
            self.state = 279
            self.labelNameList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelNameContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyword(self):
            return self.getTypedRuleContext(PromQLParser.KeywordContext, 0)

        def METRIC_NAME(self):
            return self.getToken(PromQLParser.METRIC_NAME, 0)

        def LABEL_NAME(self):
            return self.getToken(PromQLParser.LABEL_NAME, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_labelName

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLabelName"):
                listener.enterLabelName(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLabelName"):
                listener.exitLabelName(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLabelName"):
                return visitor.visitLabelName(self)
            else:
                return visitor.visitChildren(self)

    def labelName(self):

        localctx = PromQLParser.LabelNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_labelName)
        try:
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                PromQLParser.AND,
                PromQLParser.OR,
                PromQLParser.UNLESS,
                PromQLParser.BY,
                PromQLParser.WITHOUT,
                PromQLParser.ON,
                PromQLParser.IGNORING,
                PromQLParser.GROUP_LEFT,
                PromQLParser.GROUP_RIGHT,
                PromQLParser.OFFSET,
                PromQLParser.BOOL,
                PromQLParser.AGGREGATION_OPERATOR,
                PromQLParser.FUNCTION,
            ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.keyword()
                pass
            elif token in [PromQLParser.METRIC_NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.match(PromQLParser.METRIC_NAME)
                pass
            elif token in [PromQLParser.LABEL_NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 283
                self.match(PromQLParser.LABEL_NAME)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelNameListContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(PromQLParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(PromQLParser.RIGHT_PAREN, 0)

        def labelName(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PromQLParser.LabelNameContext)
            else:
                return self.getTypedRuleContext(PromQLParser.LabelNameContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(PromQLParser.COMMA)
            else:
                return self.getToken(PromQLParser.COMMA, i)

        def getRuleIndex(self):
            return PromQLParser.RULE_labelNameList

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLabelNameList"):
                listener.enterLabelNameList(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLabelNameList"):
                listener.exitLabelNameList(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLabelNameList"):
                return visitor.visitLabelNameList(self)
            else:
                return visitor.visitChildren(self)

    def labelNameList(self):

        localctx = PromQLParser.LabelNameListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_labelNameList)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(PromQLParser.LEFT_PAREN)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3F) == 0 and (
                (1 << _la)
                & (
                    (1 << PromQLParser.AND)
                    | (1 << PromQLParser.OR)
                    | (1 << PromQLParser.UNLESS)
                    | (1 << PromQLParser.BY)
                    | (1 << PromQLParser.WITHOUT)
                    | (1 << PromQLParser.ON)
                    | (1 << PromQLParser.IGNORING)
                    | (1 << PromQLParser.GROUP_LEFT)
                    | (1 << PromQLParser.GROUP_RIGHT)
                    | (1 << PromQLParser.OFFSET)
                    | (1 << PromQLParser.BOOL)
                    | (1 << PromQLParser.AGGREGATION_OPERATOR)
                    | (1 << PromQLParser.FUNCTION)
                    | (1 << PromQLParser.METRIC_NAME)
                    | (1 << PromQLParser.LABEL_NAME)
                )
            ) != 0:
                self.state = 287
                self.labelName()
                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == PromQLParser.COMMA:
                    self.state = 288
                    self.match(PromQLParser.COMMA)
                    self.state = 289
                    self.labelName()
                    self.state = 294
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 297
            self.match(PromQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeywordContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(PromQLParser.AND, 0)

        def OR(self):
            return self.getToken(PromQLParser.OR, 0)

        def UNLESS(self):
            return self.getToken(PromQLParser.UNLESS, 0)

        def BY(self):
            return self.getToken(PromQLParser.BY, 0)

        def WITHOUT(self):
            return self.getToken(PromQLParser.WITHOUT, 0)

        def ON(self):
            return self.getToken(PromQLParser.ON, 0)

        def IGNORING(self):
            return self.getToken(PromQLParser.IGNORING, 0)

        def GROUP_LEFT(self):
            return self.getToken(PromQLParser.GROUP_LEFT, 0)

        def GROUP_RIGHT(self):
            return self.getToken(PromQLParser.GROUP_RIGHT, 0)

        def OFFSET(self):
            return self.getToken(PromQLParser.OFFSET, 0)

        def BOOL(self):
            return self.getToken(PromQLParser.BOOL, 0)

        def AGGREGATION_OPERATOR(self):
            return self.getToken(PromQLParser.AGGREGATION_OPERATOR, 0)

        def FUNCTION(self):
            return self.getToken(PromQLParser.FUNCTION, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_keyword

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterKeyword"):
                listener.enterKeyword(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitKeyword"):
                listener.exitKeyword(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitKeyword"):
                return visitor.visitKeyword(self)
            else:
                return visitor.visitChildren(self)

    def keyword(self):

        localctx = PromQLParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_keyword)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            _la = self._input.LA(1)
            if not (
                (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << PromQLParser.AND)
                            | (1 << PromQLParser.OR)
                            | (1 << PromQLParser.UNLESS)
                            | (1 << PromQLParser.BY)
                            | (1 << PromQLParser.WITHOUT)
                            | (1 << PromQLParser.ON)
                            | (1 << PromQLParser.IGNORING)
                            | (1 << PromQLParser.GROUP_LEFT)
                            | (1 << PromQLParser.GROUP_RIGHT)
                            | (1 << PromQLParser.OFFSET)
                            | (1 << PromQLParser.BOOL)
                            | (1 << PromQLParser.AGGREGATION_OPERATOR)
                            | (1 << PromQLParser.FUNCTION)
                        )
                    )
                    != 0
                )
            ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(PromQLParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(PromQLParser.STRING, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_literal

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLiteral"):
                listener.enterLiteral(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLiteral"):
                listener.exitLiteral(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLiteral"):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)

    def literal(self):

        localctx = PromQLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_literal)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            _la = self._input.LA(1)
            if not (_la == PromQLParser.NUMBER or _la == PromQLParser.STRING):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.vectorOperation_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def vectorOperation_sempred(self, localctx: VectorOperationContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 10)

        if predIndex == 1:
            return self.precpred(self._ctx, 7)

        if predIndex == 2:
            return self.precpred(self._ctx, 6)

        if predIndex == 3:
            return self.precpred(self._ctx, 5)

        if predIndex == 4:
            return self.precpred(self._ctx, 4)

        if predIndex == 5:
            return self.precpred(self._ctx, 3)

        if predIndex == 6:
            return self.precpred(self._ctx, 2)

        if predIndex == 7:
            return self.precpred(self._ctx, 9)
