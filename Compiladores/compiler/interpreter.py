"""
Intérprete para Mini2DLang
Ejecuta el AST y genera comandos para el motor 2D
"""

from compiler.ast_nodes import *


class Interpreter:
    """Intérprete que ejecuta el AST"""
    
    def __init__(self, game_driver):
        self.driver = game_driver
        self.variables = {}
        self.loop_counter = 0
    
    def interpret(self, ast):
        """Ejecuta el programa completo"""
        print("=== Iniciando interpretación ===")
        self._execute_program(ast)
        print("=== Interpretación completada ===\n")
    
    def _execute_program(self, node):
        """Ejecuta el nodo Program"""
        if not isinstance(node, Program):
            raise ValueError("Se esperaba un nodo Program")
        
        for stmt in node.statements:
            self._execute_statement(stmt)
    
    def _execute_statement(self, stmt):
        """Ejecuta cada tipo de declaración"""
        if isinstance(stmt, SpriteDeclaration):
            self._execute_sprite_declaration(stmt)
        elif isinstance(stmt, EnvironmentSetting):
            self._execute_environment_setting(stmt)
        elif isinstance(stmt, ActionNode):
            self._execute_action(stmt)
        elif isinstance(stmt, IfStatement):
            self._execute_if_statement(stmt)
        elif isinstance(stmt, LoopStatement):
            self._execute_loop_statement(stmt)
    
    def _execute_sprite_declaration(self, node):
        """Crea un sprite en el motor"""
        x = self._evaluate_expr(node.x)
        y = self._evaluate_expr(node.y)
        print(f"  Creando sprite '{node.name}' en ({x}, {y})")
        self.driver.load_sprite(node.name, x, y)
    
    def _execute_environment_setting(self, node):
        """Configura el entorno del juego"""
        value = self._evaluate_expr(node.value)
        print(f"  Configurando {node.setting_name} = {value}")
        
        if node.setting_name == 'gravity':
            self.driver.set_gravity(value)
        elif node.setting_name == 'world_width':
            self.driver.set_world_width(value)
        elif node.setting_name == 'world_height':
            self.driver.set_world_height(value)
        elif node.setting_name == 'player_speed':
            self.driver.set_player_speed(value)
        
        self.variables[node.setting_name] = value
    
    def _execute_action(self, node):
        """Ejecuta una acción sobre un sprite"""
        sprite_name = node.sprite_name
        action = node.action_type
        
        if action == 'move':
            x = self._evaluate_expr(node.params[0])
            y = self._evaluate_expr(node.params[1])
            print(f"  {sprite_name}.move({x}, {y})")
            self.driver.execute_action(sprite_name, 'move', x, y)
        
        elif action == 'jump':
            print(f"  {sprite_name}.jump()")
            self.driver.execute_action(sprite_name, 'jump')
        
        elif action == 'run':
            speed = self._evaluate_expr(node.params[0])
            print(f"  {sprite_name}.run({speed})")
            self.driver.execute_action(sprite_name, 'run', speed)
        
        elif action == 'crouch':
            print(f"  {sprite_name}.crouch()")
            self.driver.execute_action(sprite_name, 'crouch')
        
        elif action == 'stop':
            print(f"  {sprite_name}.stop()")
            self.driver.execute_action(sprite_name, 'stop')
        
        elif action == 'set_animation':
            anim_name = node.params[0].value if isinstance(node.params[0], StringLiteral) else str(node.params[0])
            print(f"  {sprite_name}.set_animation('{anim_name}')")
            self.driver.execute_action(sprite_name, 'set_animation', anim_name)
    
    def _execute_if_statement(self, node):
        """Ejecuta una estructura if/else"""
        condition_result = self._evaluate_condition(node.condition)
        print(f"  if ({condition_result})")
        
        if condition_result:
            for stmt in node.true_block:
                self._execute_statement(stmt)
        else:
            for stmt in node.false_block:
                self._execute_statement(stmt)
    
    def _execute_loop_statement(self, node):
        """Ejecuta un bucle"""
        iterations = int(self._evaluate_expr(node.iterations))
        print(f"  loop {iterations} veces")
        
        for i in range(iterations):
            self.loop_counter = i
            for stmt in node.body:
                self._execute_statement(stmt)
    
    def _evaluate_expr(self, expr):
        """Evalúa una expresión y retorna su valor"""
        if isinstance(expr, NumberLiteral):
            return expr.value
        
        elif isinstance(expr, StringLiteral):
            return expr.value
        
        elif isinstance(expr, Identifier):
            if expr.name == 'loop_counter':
                return self.loop_counter
            return self.variables.get(expr.name, 0)
        
        elif isinstance(expr, BinaryOp):
            left = self._evaluate_expr(expr.left)
            right = self._evaluate_expr(expr.right)
            
            if expr.operator == '+':
                return left + right
            elif expr.operator == '-':
                return left - right
            elif expr.operator == '*':
                return left * right
            elif expr.operator == '/':
                return left / right if right != 0 else 0
        
        return 0
    
    def _evaluate_condition(self, condition):
        """Evalúa una condición y retorna True/False"""
        if isinstance(condition, Condition):
            left = self._evaluate_expr(condition.left)
            right = self._evaluate_expr(condition.right)
            
            if condition.operator == '==':
                return left == right
            elif condition.operator == '!=':
                return left != right
            elif condition.operator == '<':
                return left < right
            elif condition.operator == '>':
                return left > right
            elif condition.operator == '<=':
                return left <= right
            elif condition.operator == '>=':
                return left >= right
        
        # Si es una expresión simple, verifica si es verdadera
        return bool(self._evaluate_expr(condition))
