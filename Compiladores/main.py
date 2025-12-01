"""
Main - Compilador Mini2DLang
Punto de entrada principal del compilador
"""

import sys
from antlr4 import *
from grammar.Mini2DLangLexer import Mini2DLangLexer
from grammar.Mini2DLangParser import Mini2DLangParser
from compiler.ast_nodes import *
from compiler.semantic_analyzer import SemanticAnalyzer
from compiler.interpreter import Interpreter
from engine.game_driver import GameDriver


class ASTBuilder:
    """Constructor del AST a partir del árbol de sintaxis concreta"""
    
    def build(self, ctx):
        """Construye el AST desde el contexto del parser"""
        if isinstance(ctx, Mini2DLangParser.ProgramContext):
            statements = []
            for stmt in ctx.statement():
                node = self.build_statement(stmt)
                if node:
                    statements.append(node)
            return Program(statements)
        return None
    
    def build_statement(self, ctx):
        """Construye un nodo de declaración"""
        if ctx.spriteDeclaration():
            return self.build_sprite_declaration(ctx.spriteDeclaration())
        elif ctx.environmentSetting():
            return self.build_environment_setting(ctx.environmentSetting())
        elif ctx.action():
            return self.build_action(ctx.action())
        elif ctx.controlFlow():
            return self.build_control_flow(ctx.controlFlow())
        return None
    
    def build_sprite_declaration(self, ctx):
        """Construye SpriteDeclaration"""
        name = ctx.IDENTIFIER().getText()
        x_expr = self.build_expr(ctx.expr(0))
        y_expr = self.build_expr(ctx.expr(1))
        return SpriteDeclaration(name, x_expr, y_expr)
    
    def build_environment_setting(self, ctx):
        """Construye EnvironmentSetting"""
        if ctx.GRAVITY():
            setting_name = "gravity"
        elif ctx.WORLD_WIDTH():
            setting_name = "world_width"
        elif ctx.WORLD_HEIGHT():
            setting_name = "world_height"
        elif ctx.PLAYER_SPEED():
            setting_name = "player_speed"
        else:
            return None
        
        value = self.build_expr(ctx.expr())
        return EnvironmentSetting(setting_name, value)
    
    def build_action(self, ctx):
        """Construye ActionNode"""
        sprite_name = ctx.IDENTIFIER().getText()
        
        if ctx.MOVE():
            action_type = "move"
            params = [self.build_expr(ctx.expr(0)), self.build_expr(ctx.expr(1))]
        elif ctx.JUMP():
            action_type = "jump"
            params = []
        elif ctx.RUN():
            action_type = "run"
            params = [self.build_expr(ctx.expr())]
        elif ctx.CROUCH():
            action_type = "crouch"
            params = []
        elif ctx.STOP():
            action_type = "stop"
            params = []
        elif ctx.SET_ANIMATION():
            action_type = "set_animation"
            string_val = ctx.STRING().getText()
            params = [StringLiteral(string_val)]
        else:
            return None
        
        return ActionNode(sprite_name, action_type, params)
    
    def build_control_flow(self, ctx):
        """Construye nodos de control de flujo"""
        if ctx.ifStatement():
            return self.build_if_statement(ctx.ifStatement())
        elif ctx.loopStatement():
            return self.build_loop_statement(ctx.loopStatement())
        return None
    
    def build_if_statement(self, ctx):
        """Construye IfStatement"""
        condition = self.build_condition(ctx.condition())
        
        true_block = []
        for stmt in ctx.statement():
            node = self.build_statement(stmt)
            if node:
                true_block.append(node)
        
        false_block = []
        if ctx.ELSE():
            # Los statements después del ELSE
            else_start = len(ctx.statement()) // 2 if len(ctx.statement()) > 1 else 0
            for i in range(else_start, len(ctx.statement())):
                node = self.build_statement(ctx.statement(i))
                if node:
                    false_block.append(node)
        
        return IfStatement(condition, true_block, false_block)
    
    def build_loop_statement(self, ctx):
        """Construye LoopStatement"""
        iterations = self.build_expr(ctx.expr())
        
        body = []
        for stmt in ctx.statement():
            node = self.build_statement(stmt)
            if node:
                body.append(node)
        
        return LoopStatement(iterations, body)
    
    def build_condition(self, ctx):
        """Construye Condition"""
        if ctx.comparator():
            left = self.build_expr(ctx.expr(0))
            operator = ctx.comparator().getText()
            right = self.build_expr(ctx.expr(1))
            return Condition(left, operator, right)
        else:
            return self.build_expr(ctx.expr(0))
    
    def build_expr(self, ctx):
        """Construye expresiones"""
        if isinstance(ctx, Mini2DLangParser.NumberContext):
            return NumberLiteral(ctx.NUMBER().getText())
        
        elif isinstance(ctx, Mini2DLangParser.IdentifierContext):
            return Identifier(ctx.IDENTIFIER().getText())
        
        elif isinstance(ctx, Mini2DLangParser.ParensContext):
            return self.build_expr(ctx.expr())
        
        elif isinstance(ctx, Mini2DLangParser.MulDivContext):
            left = self.build_expr(ctx.expr(0))
            operator = ctx.MULT().getText() if ctx.MULT() else ctx.DIV().getText()
            right = self.build_expr(ctx.expr(1))
            return BinaryOp(left, operator, right)
        
        elif isinstance(ctx, Mini2DLangParser.AddSubContext):
            left = self.build_expr(ctx.expr(0))
            operator = ctx.PLUS().getText() if ctx.PLUS() else ctx.MINUS().getText()
            right = self.build_expr(ctx.expr(1))
            return BinaryOp(left, operator, right)
        
        return NumberLiteral("0")


def compile_and_run(script_path, run_duration=10):
    """Compila y ejecuta un script de Mini2DLang"""
    
    print("=" * 60)
    print("COMPILADOR MINI2DLANG")
    print("=" * 60)
    
    # 1. Cargar el script
    print(f"\n[1/6] Cargando script: {script_path}")
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            script_content = f.read()
        print(f"✓ Script cargado ({len(script_content)} caracteres)")
    except FileNotFoundError:
        print(f"✗ Error: No se encontró el archivo {script_path}")
        return
    
    # 2. Análisis Léxico
    print("\n[2/6] Análisis Léxico (Lexer)")
    input_stream = InputStream(script_content)
    lexer = Mini2DLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    tokens = token_stream.tokens
    print(f"✓ Se encontraron {len(tokens)} tokens")
    print("\nPrimeros 10 tokens:")
    for i, token in enumerate(tokens[:10]):
        token_name = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else "UNKNOWN"
        print(f"  {i+1}. {token_name}: '{token.text}'")
    
    # 3. Análisis Sintáctico
    print("\n[3/6] Análisis Sintáctico (Parser)")
    parser = Mini2DLangParser(token_stream)
    tree = parser.program()
    print(f"✓ Árbol de sintaxis concreta generado")
    print(f"  Número de hijos: {tree.getChildCount()}")
    
    # 4. Construcción del AST
    print("\n[4/6] Construcción del AST")
    ast_builder = ASTBuilder()
    ast = ast_builder.build(tree)
    print(f"✓ AST construido con {len(ast.statements)} declaraciones")
    print("\nEstructura del AST:")
    for i, stmt in enumerate(ast.statements[:5]):
        print(f"  {i+1}. {stmt}")
    
    # 5. Análisis Semántico
    print("\n[5/6] Análisis Semántico")
    semantic_analyzer = SemanticAnalyzer()
    if not semantic_analyzer.analyze(ast):
        print("✗ El análisis semántico falló. Abortando.")
        return
    
    # 6. Interpretación y Ejecución
    print("\n[6/6] Interpretación y Ejecución")
    
    # Inicializar motor 2D
    game_driver = GameDriver(width=800, height=600, title="Mini2DLang Engine")
    
    # Crear intérprete
    interpreter = Interpreter(game_driver)
    
    # Interpretar el AST
    interpreter.interpret(ast)
    
    # Ejecutar el motor
    print(f"\n⚡ Iniciando motor 2D...")
    game_driver.run(duration_seconds=run_duration)
    
    print("\n" + "=" * 60)
    print("COMPILACIÓN Y EJECUCIÓN COMPLETADA")
    print("=" * 60)


if __name__ == "__main__":
    # Ejecutar con el script de ejemplo
    script_file = "example_script.m2d"
    
    if len(sys.argv) > 1:
        script_file = sys.argv[1]
    
    compile_and_run(script_file, run_duration=15)
