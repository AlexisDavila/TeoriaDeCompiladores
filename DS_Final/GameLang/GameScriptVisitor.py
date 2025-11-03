# Generated from GameScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GameScriptParser import GameScriptParser
else:
    from GameScriptParser import GameScriptParser

# This class defines a complete generic visitor for a parse tree produced by GameScriptParser.

class GameScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GameScriptParser#script.
    def visitScript(self, ctx:GameScriptParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameScriptParser#command.
    def visitCommand(self, ctx:GameScriptParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameScriptParser#moveCommand.
    def visitMoveCommand(self, ctx:GameScriptParser.MoveCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameScriptParser#jumpCommand.
    def visitJumpCommand(self, ctx:GameScriptParser.JumpCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameScriptParser#attackCommand.
    def visitAttackCommand(self, ctx:GameScriptParser.AttackCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameScriptParser#waitCommand.
    def visitWaitCommand(self, ctx:GameScriptParser.WaitCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameScriptParser#direction.
    def visitDirection(self, ctx:GameScriptParser.DirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameScriptParser#target.
    def visitTarget(self, ctx:GameScriptParser.TargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameScriptParser#amount.
    def visitAmount(self, ctx:GameScriptParser.AmountContext):
        return self.visitChildren(ctx)



del GameScriptParser