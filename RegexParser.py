# Generated from Regex.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("\31\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\13\n\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\2\2")
        buf.write("\3\2\3\2\2\2\2\33\2\n\3\2\2\2\4\5\b\2\1\2\5\6\7\3\2\2")
        buf.write("\6\7\5\2\2\2\7\b\7\4\2\2\b\13\3\2\2\2\t\13\7\5\2\2\n\4")
        buf.write("\3\2\2\2\n\t\3\2\2\2\13\25\3\2\2\2\f\r\f\5\2\2\r\24\5")
        buf.write("\2\2\6\16\17\f\4\2\2\17\20\7\6\2\2\20\24\5\2\2\5\21\22")
        buf.write("\f\7\2\2\22\24\7\7\2\2\23\f\3\2\2\2\23\16\3\2\2\2\23\21")
        buf.write("\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26")
        buf.write("\3\3\2\2\2\27\25\3\2\2\2\5\n\23\25")
        return buf.getvalue()


class RegexParser ( Parser ):

    grammarFileName = "Regex.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "'|'", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "REGEX_ATOM", 
                      "OR", "KLEENSTAR" ]

    RULE_regex = 0

    ruleNames =  [ "regex" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    REGEX_ATOM=3
    OR=4
    KLEENSTAR=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RegexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegexParser.RULE_regex

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class RegexOrContext(RegexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegexParser.RegexContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def regex(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegexParser.RegexContext)
            else:
                return self.getTypedRuleContext(RegexParser.RegexContext,i)

        def OR(self):
            return self.getToken(RegexParser.OR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegexOr" ):
                return visitor.visitRegexOr(self)
            else:
                return visitor.visitChildren(self)


    class RegexStarContext(RegexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegexParser.RegexContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def regex(self):
            return self.getTypedRuleContext(RegexParser.RegexContext,0)

        def KLEENSTAR(self):
            return self.getToken(RegexParser.KLEENSTAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegexStar" ):
                return visitor.visitRegexStar(self)
            else:
                return visitor.visitChildren(self)


    class RegexParanthContext(RegexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegexParser.RegexContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def regex(self):
            return self.getTypedRuleContext(RegexParser.RegexContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegexParanth" ):
                return visitor.visitRegexParanth(self)
            else:
                return visitor.visitChildren(self)


    class RegexConcatContext(RegexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegexParser.RegexContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def regex(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegexParser.RegexContext)
            else:
                return self.getTypedRuleContext(RegexParser.RegexContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegexConcat" ):
                return visitor.visitRegexConcat(self)
            else:
                return visitor.visitChildren(self)


    class RegexAtomContext(RegexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegexParser.RegexContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REGEX_ATOM(self):
            return self.getToken(RegexParser.REGEX_ATOM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegexAtom" ):
                return visitor.visitRegexAtom(self)
            else:
                return visitor.visitChildren(self)



    def regex(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RegexParser.RegexContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_regex, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RegexParser.T__0]:
                localctx = RegexParser.RegexParanthContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                self.match(RegexParser.T__0)
                self.state = 4
                self.regex(0)
                self.state = 5
                self.match(RegexParser.T__1)
                pass
            elif token in [RegexParser.REGEX_ATOM]:
                localctx = RegexParser.RegexAtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                self.match(RegexParser.REGEX_ATOM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 17
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = RegexParser.RegexConcatContext(self, RegexParser.RegexContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_regex)
                        self.state = 10
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 11
                        self.regex(4)
                        pass

                    elif la_ == 2:
                        localctx = RegexParser.RegexOrContext(self, RegexParser.RegexContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_regex)
                        self.state = 12
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 13
                        self.match(RegexParser.OR)
                        self.state = 14
                        self.regex(3)
                        pass

                    elif la_ == 3:
                        localctx = RegexParser.RegexStarContext(self, RegexParser.RegexContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_regex)
                        self.state = 15
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 16
                        self.match(RegexParser.KLEENSTAR)
                        pass

             
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.regex_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def regex_sempred(self, localctx:RegexContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




