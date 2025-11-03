import sys
from antlr4 import *
from GameScriptLexer import GameScriptLexer
from GameScriptParser import GameScriptParser
from GameScriptVisitor import GameScriptVisitor

class GameActionVisitor(GameScriptVisitor):
    def visitMoveCommand(self, ctx: GameScriptParser.MoveCommandContext):
        direction = ctx.direction().getText()
        amount = ctx.amount().getText()
        print(f"Action: MOVE, Direction: {direction}, Steps: {amount}")
        return None

    def visitJumpCommand(self, ctx: GameScriptParser.JumpCommandContext):
        print("Action: JUMP")
        return None

    def visitAttackCommand(self, ctx: GameScriptParser.AttackCommandContext):
        target = ctx.target().getText()
        print(f"Action: ATTACK, Target: {target}")
        return None

    def visitWaitCommand(self, ctx: GameScriptParser.WaitCommandContext):
        amount = ctx.amount().getText()
        print(f"Action: WAIT, Duration: {amount} seconds")
        return None


def main():
    input_stream = FileStream("test.tp")
    lexer = GameScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GameScriptParser(stream)
    tree = parser.script()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("❌ El script contiene errores de sintaxis.")
        return

    print("✅ Script analizado exitosamente. Ejecutando acciones...\n")
    visitor = GameActionVisitor()
    visitor.visit(tree)
    print("\n🏁 Ejecución finalizada.")


if __name__ == "__main__":
    main()
