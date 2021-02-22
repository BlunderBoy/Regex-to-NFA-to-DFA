# Generated from Regex.g by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("\27\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3")
        buf.write("\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\2\2\7\3\3\5\4\7\5\t")
        buf.write("\6\13\7\3\2\3\3\2c|\2\26\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\3\r\3\2\2\2\5\17\3\2\2")
        buf.write("\2\7\21\3\2\2\2\t\23\3\2\2\2\13\25\3\2\2\2\r\16\7*\2\2")
        buf.write("\16\4\3\2\2\2\17\20\7+\2\2\20\6\3\2\2\2\21\22\t\2\2\2")
        buf.write("\22\b\3\2\2\2\23\24\7~\2\2\24\n\3\2\2\2\25\26\7,\2\2\26")
        buf.write("\f\3\2\2\2\3\2\2")
        return buf.getvalue()


class RegexLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    REGEX_ATOM = 3
    OR = 4
    KLEENSTAR = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'|'", "'*'" ]

    symbolicNames = [ "<INVALID>",
            "REGEX_ATOM", "OR", "KLEENSTAR" ]

    ruleNames = [ "T__0", "T__1", "REGEX_ATOM", "OR", "KLEENSTAR" ]

    grammarFileName = "Regex.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


