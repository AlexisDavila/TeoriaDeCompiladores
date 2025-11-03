# Generated from GameScript.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,0,1,0,1,1,1,1,1,
        1,1,1,3,1,30,8,1,1,2,1,2,1,2,1,2,4,2,36,8,2,11,2,12,2,37,1,3,1,3,
        4,3,42,8,3,11,3,12,3,43,1,4,1,4,1,4,4,4,49,8,4,11,4,12,4,50,1,5,
        1,5,1,5,1,5,4,5,57,8,5,11,5,12,5,58,1,6,1,6,1,7,1,7,1,8,1,8,1,8,
        0,0,9,0,2,4,6,8,10,12,14,16,0,3,2,0,2,2,15,15,1,0,7,10,1,0,11,13,
        65,0,19,1,0,0,0,2,29,1,0,0,0,4,31,1,0,0,0,6,39,1,0,0,0,8,45,1,0,
        0,0,10,52,1,0,0,0,12,60,1,0,0,0,14,62,1,0,0,0,16,64,1,0,0,0,18,20,
        3,2,1,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,
        22,23,1,0,0,0,23,24,5,0,0,1,24,1,1,0,0,0,25,30,3,4,2,0,26,30,3,6,
        3,0,27,30,3,8,4,0,28,30,3,10,5,0,29,25,1,0,0,0,29,26,1,0,0,0,29,
        27,1,0,0,0,29,28,1,0,0,0,30,3,1,0,0,0,31,32,5,1,0,0,32,33,3,12,6,
        0,33,35,3,16,8,0,34,36,7,0,0,0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,
        1,0,0,0,37,38,1,0,0,0,38,5,1,0,0,0,39,41,5,3,0,0,40,42,7,0,0,0,41,
        40,1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,7,1,0,0,
        0,45,46,5,4,0,0,46,48,3,14,7,0,47,49,7,0,0,0,48,47,1,0,0,0,49,50,
        1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,9,1,0,0,0,52,53,5,5,0,0,53,
        54,3,16,8,0,54,56,5,6,0,0,55,57,7,0,0,0,56,55,1,0,0,0,57,58,1,0,
        0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,11,1,0,0,0,60,61,7,1,0,0,61,13,
        1,0,0,0,62,63,7,2,0,0,63,15,1,0,0,0,64,65,5,14,0,0,65,17,1,0,0,0,
        6,21,29,37,43,50,58
    ]

class GameScriptParser ( Parser ):

    grammarFileName = "GameScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'move'", "';'", "'jump'", "'attack'", 
                     "'wait'", "'seconds'", "'left'", "'right'", "'up'", 
                     "'down'", "'enemy'", "'boss'", "'object'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "NEWLINE", "WS" ]

    RULE_script = 0
    RULE_command = 1
    RULE_moveCommand = 2
    RULE_jumpCommand = 3
    RULE_attackCommand = 4
    RULE_waitCommand = 5
    RULE_direction = 6
    RULE_target = 7
    RULE_amount = 8

    ruleNames =  [ "script", "command", "moveCommand", "jumpCommand", "attackCommand", 
                   "waitCommand", "direction", "target", "amount" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    INT=14
    NEWLINE=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GameScriptParser.EOF, 0)

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GameScriptParser.CommandContext)
            else:
                return self.getTypedRuleContext(GameScriptParser.CommandContext,i)


        def getRuleIndex(self):
            return GameScriptParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScript" ):
                return visitor.visitScript(self)
            else:
                return visitor.visitChildren(self)




    def script(self):

        localctx = GameScriptParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.command()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 58) != 0)):
                    break

            self.state = 23
            self.match(GameScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def moveCommand(self):
            return self.getTypedRuleContext(GameScriptParser.MoveCommandContext,0)


        def jumpCommand(self):
            return self.getTypedRuleContext(GameScriptParser.JumpCommandContext,0)


        def attackCommand(self):
            return self.getTypedRuleContext(GameScriptParser.AttackCommandContext,0)


        def waitCommand(self):
            return self.getTypedRuleContext(GameScriptParser.WaitCommandContext,0)


        def getRuleIndex(self):
            return GameScriptParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = GameScriptParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.moveCommand()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.jumpCommand()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.attackCommand()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.waitCommand()
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


    class MoveCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def direction(self):
            return self.getTypedRuleContext(GameScriptParser.DirectionContext,0)


        def amount(self):
            return self.getTypedRuleContext(GameScriptParser.AmountContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(GameScriptParser.NEWLINE)
            else:
                return self.getToken(GameScriptParser.NEWLINE, i)

        def getRuleIndex(self):
            return GameScriptParser.RULE_moveCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoveCommand" ):
                listener.enterMoveCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoveCommand" ):
                listener.exitMoveCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveCommand" ):
                return visitor.visitMoveCommand(self)
            else:
                return visitor.visitChildren(self)




    def moveCommand(self):

        localctx = GameScriptParser.MoveCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_moveCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(GameScriptParser.T__0)
            self.state = 32
            self.direction()
            self.state = 33
            self.amount()
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                _la = self._input.LA(1)
                if not(_la==2 or _la==15):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==15):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JumpCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(GameScriptParser.NEWLINE)
            else:
                return self.getToken(GameScriptParser.NEWLINE, i)

        def getRuleIndex(self):
            return GameScriptParser.RULE_jumpCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJumpCommand" ):
                listener.enterJumpCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJumpCommand" ):
                listener.exitJumpCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJumpCommand" ):
                return visitor.visitJumpCommand(self)
            else:
                return visitor.visitChildren(self)




    def jumpCommand(self):

        localctx = GameScriptParser.JumpCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_jumpCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(GameScriptParser.T__2)
            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                _la = self._input.LA(1)
                if not(_la==2 or _la==15):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==15):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttackCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def target(self):
            return self.getTypedRuleContext(GameScriptParser.TargetContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(GameScriptParser.NEWLINE)
            else:
                return self.getToken(GameScriptParser.NEWLINE, i)

        def getRuleIndex(self):
            return GameScriptParser.RULE_attackCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttackCommand" ):
                listener.enterAttackCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttackCommand" ):
                listener.exitAttackCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttackCommand" ):
                return visitor.visitAttackCommand(self)
            else:
                return visitor.visitChildren(self)




    def attackCommand(self):

        localctx = GameScriptParser.AttackCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attackCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(GameScriptParser.T__3)
            self.state = 46
            self.target()
            self.state = 48 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 47
                _la = self._input.LA(1)
                if not(_la==2 or _la==15):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 50 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==15):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WaitCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def amount(self):
            return self.getTypedRuleContext(GameScriptParser.AmountContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(GameScriptParser.NEWLINE)
            else:
                return self.getToken(GameScriptParser.NEWLINE, i)

        def getRuleIndex(self):
            return GameScriptParser.RULE_waitCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWaitCommand" ):
                listener.enterWaitCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWaitCommand" ):
                listener.exitWaitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWaitCommand" ):
                return visitor.visitWaitCommand(self)
            else:
                return visitor.visitChildren(self)




    def waitCommand(self):

        localctx = GameScriptParser.WaitCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_waitCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(GameScriptParser.T__4)
            self.state = 53
            self.amount()
            self.state = 54
            self.match(GameScriptParser.T__5)
            self.state = 56 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                _la = self._input.LA(1)
                if not(_la==2 or _la==15):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==15):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GameScriptParser.RULE_direction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirection" ):
                listener.enterDirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirection" ):
                listener.exitDirection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirection" ):
                return visitor.visitDirection(self)
            else:
                return visitor.visitChildren(self)




    def direction(self):

        localctx = GameScriptParser.DirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_direction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0)):
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


    class TargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GameScriptParser.RULE_target

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTarget" ):
                listener.enterTarget(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTarget" ):
                listener.exitTarget(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTarget" ):
                return visitor.visitTarget(self)
            else:
                return visitor.visitChildren(self)




    def target(self):

        localctx = GameScriptParser.TargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_target)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
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


    class AmountContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GameScriptParser.INT, 0)

        def getRuleIndex(self):
            return GameScriptParser.RULE_amount

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAmount" ):
                listener.enterAmount(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAmount" ):
                listener.exitAmount(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAmount" ):
                return visitor.visitAmount(self)
            else:
                return visitor.visitChildren(self)




    def amount(self):

        localctx = GameScriptParser.AmountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_amount)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(GameScriptParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





