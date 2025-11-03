import sys
import antlr4
import time
from GameLang.GameScriptLexer import GameScriptLexer
from GameLang.GameScriptParser import GameScriptParser
from engine.interpreter import GameEngine

class GameVisitor(antlr4.ParseTreeVisitor):
    def __init__(self, engine):
        self.engine = engine

    def visitMoveCommand(self, ctx):
        direction = ctx.direction().getText()
        steps = int(ctx.amount().getText())
        print(f"🚶 Moviendo {direction} {steps} pasos")
        self.engine.move(direction, steps)
        return None  

    def visitJumpCommand(self, ctx):
        print("🦘 Saltando")
        self.engine.jump()
        return None

    def visitAttackCommand(self, ctx):
        target = ctx.target().getText()
        print(f"⚔️ Atacando a {target}")
        self.engine.attack(target)
        return None

    def visitWaitCommand(self, ctx):
        seconds = int(ctx.amount().getText())
        print(f"⏳ Esperando {seconds} segundos...")
        self.engine.wait(seconds)
        return None


def run_script(file_path):
    input_stream = antlr4.FileStream(file_path, encoding='utf-8')
    lexer = GameScriptLexer(input_stream)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = GameScriptParser(tokens)
    tree = parser.script()

    engine = GameEngine()
    visitor = GameVisitor(engine)

    # ✅ Recorremos los comandos una sola vez
    for cmd in tree.command():
        visitor.visit(cmd)
        engine.update()
        time.sleep(0.5)

    # Mantiene la ventana abierta
    while engine.running:
        engine.update()



if __name__ == "__main__":
    run_script("scripts/test1.tp")
