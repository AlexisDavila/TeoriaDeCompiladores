# Generated from GameScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GameScriptParser import GameScriptParser
else:
    from GameScriptParser import GameScriptParser

# This class defines a complete listener for a parse tree produced by GameScriptParser.
class GameScriptListener(ParseTreeListener):

    # Enter a parse tree produced by GameScriptParser#script.
    def enterScript(self, ctx:GameScriptParser.ScriptContext):
        pass

    # Exit a parse tree produced by GameScriptParser#script.
    def exitScript(self, ctx:GameScriptParser.ScriptContext):
        pass


    # Enter a parse tree produced by GameScriptParser#command.
    def enterCommand(self, ctx:GameScriptParser.CommandContext):
        pass

    # Exit a parse tree produced by GameScriptParser#command.
    def exitCommand(self, ctx:GameScriptParser.CommandContext):
        pass


    # Enter a parse tree produced by GameScriptParser#moveCommand.
    def enterMoveCommand(self, ctx:GameScriptParser.MoveCommandContext):
        pass

    # Exit a parse tree produced by GameScriptParser#moveCommand.
    def exitMoveCommand(self, ctx:GameScriptParser.MoveCommandContext):
        pass


    # Enter a parse tree produced by GameScriptParser#jumpCommand.
    def enterJumpCommand(self, ctx:GameScriptParser.JumpCommandContext):
        pass

    # Exit a parse tree produced by GameScriptParser#jumpCommand.
    def exitJumpCommand(self, ctx:GameScriptParser.JumpCommandContext):
        pass


    # Enter a parse tree produced by GameScriptParser#attackCommand.
    def enterAttackCommand(self, ctx:GameScriptParser.AttackCommandContext):
        pass

    # Exit a parse tree produced by GameScriptParser#attackCommand.
    def exitAttackCommand(self, ctx:GameScriptParser.AttackCommandContext):
        pass


    # Enter a parse tree produced by GameScriptParser#waitCommand.
    def enterWaitCommand(self, ctx:GameScriptParser.WaitCommandContext):
        pass

    # Exit a parse tree produced by GameScriptParser#waitCommand.
    def exitWaitCommand(self, ctx:GameScriptParser.WaitCommandContext):
        pass


    # Enter a parse tree produced by GameScriptParser#direction.
    def enterDirection(self, ctx:GameScriptParser.DirectionContext):
        pass

    # Exit a parse tree produced by GameScriptParser#direction.
    def exitDirection(self, ctx:GameScriptParser.DirectionContext):
        pass


    # Enter a parse tree produced by GameScriptParser#target.
    def enterTarget(self, ctx:GameScriptParser.TargetContext):
        pass

    # Exit a parse tree produced by GameScriptParser#target.
    def exitTarget(self, ctx:GameScriptParser.TargetContext):
        pass


    # Enter a parse tree produced by GameScriptParser#amount.
    def enterAmount(self, ctx:GameScriptParser.AmountContext):
        pass

    # Exit a parse tree produced by GameScriptParser#amount.
    def exitAmount(self, ctx:GameScriptParser.AmountContext):
        pass



del GameScriptParser