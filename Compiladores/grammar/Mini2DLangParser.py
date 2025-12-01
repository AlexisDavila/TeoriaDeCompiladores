# Generated from Mini2DLangParser.g4 by ANTLR 4.13.1
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
        4,1,40,168,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,35,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,3,3,62,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,101,8,4,1,5,1,5,3,5,
        105,8,5,1,6,1,6,1,6,1,6,5,6,111,8,6,10,6,12,6,114,9,6,1,6,1,6,1,
        6,1,6,5,6,120,8,6,10,6,12,6,123,9,6,1,6,3,6,126,8,6,1,7,1,7,1,7,
        1,7,5,7,132,8,7,10,7,12,7,135,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,
        8,144,8,8,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,155,8,
        10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,163,8,10,10,10,12,10,166,9,
        10,1,10,0,1,20,11,0,2,4,6,8,10,12,14,16,18,20,0,3,1,0,25,30,1,0,
        33,34,1,0,31,32,178,0,25,1,0,0,0,2,34,1,0,0,0,4,36,1,0,0,0,6,61,
        1,0,0,0,8,100,1,0,0,0,10,104,1,0,0,0,12,106,1,0,0,0,14,127,1,0,0,
        0,16,143,1,0,0,0,18,145,1,0,0,0,20,154,1,0,0,0,22,24,3,2,1,0,23,
        22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,
        0,27,25,1,0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,35,3,4,2,0,31,35,3,
        6,3,0,32,35,3,8,4,0,33,35,3,10,5,0,34,30,1,0,0,0,34,31,1,0,0,0,34,
        32,1,0,0,0,34,33,1,0,0,0,35,3,1,0,0,0,36,37,5,1,0,0,37,38,5,37,0,
        0,38,39,5,2,0,0,39,40,5,17,0,0,40,41,3,20,10,0,41,42,5,21,0,0,42,
        43,3,20,10,0,43,44,5,18,0,0,44,5,1,0,0,0,45,46,5,12,0,0,46,47,5,
        13,0,0,47,48,5,23,0,0,48,62,3,20,10,0,49,50,5,12,0,0,50,51,5,14,
        0,0,51,52,5,23,0,0,52,62,3,20,10,0,53,54,5,12,0,0,54,55,5,15,0,0,
        55,56,5,23,0,0,56,62,3,20,10,0,57,58,5,12,0,0,58,59,5,16,0,0,59,
        60,5,23,0,0,60,62,3,20,10,0,61,45,1,0,0,0,61,49,1,0,0,0,61,53,1,
        0,0,0,61,57,1,0,0,0,62,7,1,0,0,0,63,64,5,37,0,0,64,65,5,22,0,0,65,
        66,5,3,0,0,66,67,5,17,0,0,67,68,3,20,10,0,68,69,5,21,0,0,69,70,3,
        20,10,0,70,71,5,18,0,0,71,101,1,0,0,0,72,73,5,37,0,0,73,74,5,22,
        0,0,74,75,5,4,0,0,75,76,5,17,0,0,76,101,5,18,0,0,77,78,5,37,0,0,
        78,79,5,22,0,0,79,80,5,5,0,0,80,81,5,17,0,0,81,82,3,20,10,0,82,83,
        5,18,0,0,83,101,1,0,0,0,84,85,5,37,0,0,85,86,5,22,0,0,86,87,5,6,
        0,0,87,88,5,17,0,0,88,101,5,18,0,0,89,90,5,37,0,0,90,91,5,22,0,0,
        91,92,5,7,0,0,92,93,5,17,0,0,93,101,5,18,0,0,94,95,5,37,0,0,95,96,
        5,22,0,0,96,97,5,8,0,0,97,98,5,17,0,0,98,99,5,36,0,0,99,101,5,18,
        0,0,100,63,1,0,0,0,100,72,1,0,0,0,100,77,1,0,0,0,100,84,1,0,0,0,
        100,89,1,0,0,0,100,94,1,0,0,0,101,9,1,0,0,0,102,105,3,12,6,0,103,
        105,3,14,7,0,104,102,1,0,0,0,104,103,1,0,0,0,105,11,1,0,0,0,106,
        107,5,9,0,0,107,108,3,16,8,0,108,112,5,19,0,0,109,111,3,2,1,0,110,
        109,1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,
        115,1,0,0,0,114,112,1,0,0,0,115,125,5,20,0,0,116,117,5,10,0,0,117,
        121,5,19,0,0,118,120,3,2,1,0,119,118,1,0,0,0,120,123,1,0,0,0,121,
        119,1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,121,1,0,0,0,124,
        126,5,20,0,0,125,116,1,0,0,0,125,126,1,0,0,0,126,13,1,0,0,0,127,
        128,5,11,0,0,128,129,3,20,10,0,129,133,5,19,0,0,130,132,3,2,1,0,
        131,130,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,
        134,136,1,0,0,0,135,133,1,0,0,0,136,137,5,20,0,0,137,15,1,0,0,0,
        138,139,3,20,10,0,139,140,3,18,9,0,140,141,3,20,10,0,141,144,1,0,
        0,0,142,144,3,20,10,0,143,138,1,0,0,0,143,142,1,0,0,0,144,17,1,0,
        0,0,145,146,7,0,0,0,146,19,1,0,0,0,147,148,6,10,-1,0,148,155,5,35,
        0,0,149,155,5,37,0,0,150,151,5,17,0,0,151,152,3,20,10,0,152,153,
        5,18,0,0,153,155,1,0,0,0,154,147,1,0,0,0,154,149,1,0,0,0,154,150,
        1,0,0,0,155,164,1,0,0,0,156,157,10,5,0,0,157,158,7,1,0,0,158,163,
        3,20,10,6,159,160,10,4,0,0,160,161,7,2,0,0,161,163,3,20,10,5,162,
        156,1,0,0,0,162,159,1,0,0,0,163,166,1,0,0,0,164,162,1,0,0,0,164,
        165,1,0,0,0,165,21,1,0,0,0,166,164,1,0,0,0,13,25,34,61,100,104,112,
        121,125,133,143,154,162,164
    ]

class Mini2DLangParser ( Parser ):

    grammarFileName = "Mini2DLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sprite'", "'at'", "'move'", "'jump'", 
                     "'run'", "'crouch'", "'stop'", "'set_animation'", "'if'", 
                     "'else'", "'loop'", "'set'", "'gravity'", "'world_width'", 
                     "'world_height'", "'player_speed'", "'('", "')'", "'{'", 
                     "'}'", "','", "'.'", "'='", "';'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'+'", "'-'", "'*'", 
                     "'/'" ]

    symbolicNames = [ "<INVALID>", "SPRITE", "AT", "MOVE", "JUMP", "RUN", 
                      "CROUCH", "STOP", "SET_ANIMATION", "IF", "ELSE", "LOOP", 
                      "SET", "GRAVITY", "WORLD_WIDTH", "WORLD_HEIGHT", "PLAYER_SPEED", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "COMMA", "DOT", 
                      "ASSIGN", "SEMICOLON", "EQ", "NEQ", "LT", "GT", "LTE", 
                      "GTE", "PLUS", "MINUS", "MULT", "DIV", "NUMBER", "STRING", 
                      "IDENTIFIER", "COMMENT", "BLOCK_COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_spriteDeclaration = 2
    RULE_environmentSetting = 3
    RULE_action = 4
    RULE_controlFlow = 5
    RULE_ifStatement = 6
    RULE_loopStatement = 7
    RULE_condition = 8
    RULE_comparator = 9
    RULE_expr = 10

    ruleNames =  [ "program", "statement", "spriteDeclaration", "environmentSetting", 
                   "action", "controlFlow", "ifStatement", "loopStatement", 
                   "condition", "comparator", "expr" ]

    EOF = Token.EOF
    SPRITE=1
    AT=2
    MOVE=3
    JUMP=4
    RUN=5
    CROUCH=6
    STOP=7
    SET_ANIMATION=8
    IF=9
    ELSE=10
    LOOP=11
    SET=12
    GRAVITY=13
    WORLD_WIDTH=14
    WORLD_HEIGHT=15
    PLAYER_SPEED=16
    LPAREN=17
    RPAREN=18
    LBRACE=19
    RBRACE=20
    COMMA=21
    DOT=22
    ASSIGN=23
    SEMICOLON=24
    EQ=25
    NEQ=26
    LT=27
    GT=28
    LTE=29
    GTE=30
    PLUS=31
    MINUS=32
    MULT=33
    DIV=34
    NUMBER=35
    STRING=36
    IDENTIFIER=37
    COMMENT=38
    BLOCK_COMMENT=39
    WS=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Mini2DLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mini2DLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(Mini2DLangParser.StatementContext,i)


        def getRuleIndex(self):
            return Mini2DLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = Mini2DLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137438960130) != 0):
                self.state = 22
                self.statement()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(Mini2DLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def spriteDeclaration(self):
            return self.getTypedRuleContext(Mini2DLangParser.SpriteDeclarationContext,0)


        def environmentSetting(self):
            return self.getTypedRuleContext(Mini2DLangParser.EnvironmentSettingContext,0)


        def action(self):
            return self.getTypedRuleContext(Mini2DLangParser.ActionContext,0)


        def controlFlow(self):
            return self.getTypedRuleContext(Mini2DLangParser.ControlFlowContext,0)


        def getRuleIndex(self):
            return Mini2DLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = Mini2DLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.spriteDeclaration()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.environmentSetting()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.action()
                pass
            elif token in [9, 11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.controlFlow()
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


    class SpriteDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPRITE(self):
            return self.getToken(Mini2DLangParser.SPRITE, 0)

        def IDENTIFIER(self):
            return self.getToken(Mini2DLangParser.IDENTIFIER, 0)

        def AT(self):
            return self.getToken(Mini2DLangParser.AT, 0)

        def LPAREN(self):
            return self.getToken(Mini2DLangParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mini2DLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(Mini2DLangParser.ExprContext,i)


        def COMMA(self):
            return self.getToken(Mini2DLangParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(Mini2DLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return Mini2DLangParser.RULE_spriteDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpriteDeclaration" ):
                listener.enterSpriteDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpriteDeclaration" ):
                listener.exitSpriteDeclaration(self)




    def spriteDeclaration(self):

        localctx = Mini2DLangParser.SpriteDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_spriteDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(Mini2DLangParser.SPRITE)
            self.state = 37
            self.match(Mini2DLangParser.IDENTIFIER)
            self.state = 38
            self.match(Mini2DLangParser.AT)
            self.state = 39
            self.match(Mini2DLangParser.LPAREN)
            self.state = 40
            self.expr(0)
            self.state = 41
            self.match(Mini2DLangParser.COMMA)
            self.state = 42
            self.expr(0)
            self.state = 43
            self.match(Mini2DLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnvironmentSettingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(Mini2DLangParser.SET, 0)

        def GRAVITY(self):
            return self.getToken(Mini2DLangParser.GRAVITY, 0)

        def ASSIGN(self):
            return self.getToken(Mini2DLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(Mini2DLangParser.ExprContext,0)


        def WORLD_WIDTH(self):
            return self.getToken(Mini2DLangParser.WORLD_WIDTH, 0)

        def WORLD_HEIGHT(self):
            return self.getToken(Mini2DLangParser.WORLD_HEIGHT, 0)

        def PLAYER_SPEED(self):
            return self.getToken(Mini2DLangParser.PLAYER_SPEED, 0)

        def getRuleIndex(self):
            return Mini2DLangParser.RULE_environmentSetting

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnvironmentSetting" ):
                listener.enterEnvironmentSetting(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnvironmentSetting" ):
                listener.exitEnvironmentSetting(self)




    def environmentSetting(self):

        localctx = Mini2DLangParser.EnvironmentSettingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_environmentSetting)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(Mini2DLangParser.SET)
                self.state = 46
                self.match(Mini2DLangParser.GRAVITY)
                self.state = 47
                self.match(Mini2DLangParser.ASSIGN)
                self.state = 48
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(Mini2DLangParser.SET)
                self.state = 50
                self.match(Mini2DLangParser.WORLD_WIDTH)
                self.state = 51
                self.match(Mini2DLangParser.ASSIGN)
                self.state = 52
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.match(Mini2DLangParser.SET)
                self.state = 54
                self.match(Mini2DLangParser.WORLD_HEIGHT)
                self.state = 55
                self.match(Mini2DLangParser.ASSIGN)
                self.state = 56
                self.expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.match(Mini2DLangParser.SET)
                self.state = 58
                self.match(Mini2DLangParser.PLAYER_SPEED)
                self.state = 59
                self.match(Mini2DLangParser.ASSIGN)
                self.state = 60
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Mini2DLangParser.IDENTIFIER, 0)

        def DOT(self):
            return self.getToken(Mini2DLangParser.DOT, 0)

        def MOVE(self):
            return self.getToken(Mini2DLangParser.MOVE, 0)

        def LPAREN(self):
            return self.getToken(Mini2DLangParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mini2DLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(Mini2DLangParser.ExprContext,i)


        def COMMA(self):
            return self.getToken(Mini2DLangParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(Mini2DLangParser.RPAREN, 0)

        def JUMP(self):
            return self.getToken(Mini2DLangParser.JUMP, 0)

        def RUN(self):
            return self.getToken(Mini2DLangParser.RUN, 0)

        def CROUCH(self):
            return self.getToken(Mini2DLangParser.CROUCH, 0)

        def STOP(self):
            return self.getToken(Mini2DLangParser.STOP, 0)

        def SET_ANIMATION(self):
            return self.getToken(Mini2DLangParser.SET_ANIMATION, 0)

        def STRING(self):
            return self.getToken(Mini2DLangParser.STRING, 0)

        def getRuleIndex(self):
            return Mini2DLangParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)




    def action(self):

        localctx = Mini2DLangParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_action)
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(Mini2DLangParser.IDENTIFIER)
                self.state = 64
                self.match(Mini2DLangParser.DOT)
                self.state = 65
                self.match(Mini2DLangParser.MOVE)
                self.state = 66
                self.match(Mini2DLangParser.LPAREN)
                self.state = 67
                self.expr(0)
                self.state = 68
                self.match(Mini2DLangParser.COMMA)
                self.state = 69
                self.expr(0)
                self.state = 70
                self.match(Mini2DLangParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(Mini2DLangParser.IDENTIFIER)
                self.state = 73
                self.match(Mini2DLangParser.DOT)
                self.state = 74
                self.match(Mini2DLangParser.JUMP)
                self.state = 75
                self.match(Mini2DLangParser.LPAREN)
                self.state = 76
                self.match(Mini2DLangParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.match(Mini2DLangParser.IDENTIFIER)
                self.state = 78
                self.match(Mini2DLangParser.DOT)
                self.state = 79
                self.match(Mini2DLangParser.RUN)
                self.state = 80
                self.match(Mini2DLangParser.LPAREN)
                self.state = 81
                self.expr(0)
                self.state = 82
                self.match(Mini2DLangParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.match(Mini2DLangParser.IDENTIFIER)
                self.state = 85
                self.match(Mini2DLangParser.DOT)
                self.state = 86
                self.match(Mini2DLangParser.CROUCH)
                self.state = 87
                self.match(Mini2DLangParser.LPAREN)
                self.state = 88
                self.match(Mini2DLangParser.RPAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                self.match(Mini2DLangParser.IDENTIFIER)
                self.state = 90
                self.match(Mini2DLangParser.DOT)
                self.state = 91
                self.match(Mini2DLangParser.STOP)
                self.state = 92
                self.match(Mini2DLangParser.LPAREN)
                self.state = 93
                self.match(Mini2DLangParser.RPAREN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 94
                self.match(Mini2DLangParser.IDENTIFIER)
                self.state = 95
                self.match(Mini2DLangParser.DOT)
                self.state = 96
                self.match(Mini2DLangParser.SET_ANIMATION)
                self.state = 97
                self.match(Mini2DLangParser.LPAREN)
                self.state = 98
                self.match(Mini2DLangParser.STRING)
                self.state = 99
                self.match(Mini2DLangParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ControlFlowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(Mini2DLangParser.IfStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(Mini2DLangParser.LoopStatementContext,0)


        def getRuleIndex(self):
            return Mini2DLangParser.RULE_controlFlow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterControlFlow" ):
                listener.enterControlFlow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitControlFlow" ):
                listener.exitControlFlow(self)




    def controlFlow(self):

        localctx = Mini2DLangParser.ControlFlowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_controlFlow)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.ifStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.loopStatement()
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


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(Mini2DLangParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(Mini2DLangParser.ConditionContext,0)


        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(Mini2DLangParser.LBRACE)
            else:
                return self.getToken(Mini2DLangParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(Mini2DLangParser.RBRACE)
            else:
                return self.getToken(Mini2DLangParser.RBRACE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mini2DLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(Mini2DLangParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(Mini2DLangParser.ELSE, 0)

        def getRuleIndex(self):
            return Mini2DLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = Mini2DLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(Mini2DLangParser.IF)
            self.state = 107
            self.condition()
            self.state = 108
            self.match(Mini2DLangParser.LBRACE)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137438960130) != 0):
                self.state = 109
                self.statement()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
            self.match(Mini2DLangParser.RBRACE)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 116
                self.match(Mini2DLangParser.ELSE)
                self.state = 117
                self.match(Mini2DLangParser.LBRACE)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137438960130) != 0):
                    self.state = 118
                    self.statement()
                    self.state = 123
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 124
                self.match(Mini2DLangParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOOP(self):
            return self.getToken(Mini2DLangParser.LOOP, 0)

        def expr(self):
            return self.getTypedRuleContext(Mini2DLangParser.ExprContext,0)


        def LBRACE(self):
            return self.getToken(Mini2DLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Mini2DLangParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mini2DLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(Mini2DLangParser.StatementContext,i)


        def getRuleIndex(self):
            return Mini2DLangParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)




    def loopStatement(self):

        localctx = Mini2DLangParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_loopStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(Mini2DLangParser.LOOP)
            self.state = 128
            self.expr(0)
            self.state = 129
            self.match(Mini2DLangParser.LBRACE)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137438960130) != 0):
                self.state = 130
                self.statement()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
            self.match(Mini2DLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mini2DLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(Mini2DLangParser.ExprContext,i)


        def comparator(self):
            return self.getTypedRuleContext(Mini2DLangParser.ComparatorContext,0)


        def getRuleIndex(self):
            return Mini2DLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = Mini2DLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condition)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.expr(0)
                self.state = 139
                self.comparator()
                self.state = 140
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(Mini2DLangParser.EQ, 0)

        def NEQ(self):
            return self.getToken(Mini2DLangParser.NEQ, 0)

        def LT(self):
            return self.getToken(Mini2DLangParser.LT, 0)

        def GT(self):
            return self.getToken(Mini2DLangParser.GT, 0)

        def LTE(self):
            return self.getToken(Mini2DLangParser.LTE, 0)

        def GTE(self):
            return self.getToken(Mini2DLangParser.GTE, 0)

        def getRuleIndex(self):
            return Mini2DLangParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)




    def comparator(self):

        localctx = Mini2DLangParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2113929216) != 0)):
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Mini2DLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IdentifierContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mini2DLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(Mini2DLangParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mini2DLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(Mini2DLangParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mini2DLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mini2DLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(Mini2DLangParser.ExprContext,i)

        def MULT(self):
            return self.getToken(Mini2DLangParser.MULT, 0)
        def DIV(self):
            return self.getToken(Mini2DLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mini2DLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mini2DLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(Mini2DLangParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(Mini2DLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(Mini2DLangParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mini2DLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(Mini2DLangParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(Mini2DLangParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(Mini2DLangParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Mini2DLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                localctx = Mini2DLangParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 148
                self.match(Mini2DLangParser.NUMBER)
                pass
            elif token in [37]:
                localctx = Mini2DLangParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 149
                self.match(Mini2DLangParser.IDENTIFIER)
                pass
            elif token in [17]:
                localctx = Mini2DLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 150
                self.match(Mini2DLangParser.LPAREN)
                self.state = 151
                self.expr(0)
                self.state = 152
                self.match(Mini2DLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 164
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 162
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = Mini2DLangParser.MulDivContext(self, Mini2DLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 156
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 157
                        _la = self._input.LA(1)
                        if not(_la==33 or _la==34):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 158
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = Mini2DLangParser.AddSubContext(self, Mini2DLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 159
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 160
                        _la = self._input.LA(1)
                        if not(_la==31 or _la==32):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 161
                        self.expr(5)
                        pass

             
                self.state = 166
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self._predicates[10] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




