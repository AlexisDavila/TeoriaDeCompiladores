"""
Analizador Semántico para Mini2DLang
Verifica la correctitud semántica del AST
"""

from compiler.ast_nodes import *


class SemanticError(Exception):
    """Excepción para errores semánticos"""
    pass


class SymbolTable:
    """Tabla de símbolos para sprites y variables"""
    def __init__(self):
        self.sprites = {}
        self.variables = {}
    
    def declare_sprite(self, name, x, y):
        if name in self.sprites:
            raise SemanticError(f"Sprite '{name}' ya está declarado")
        self.sprites[name] = {'x': x, 'y': y}
    
    def get_sprite(self, name):
        if name not in self.sprites:
            raise SemanticError(f"Sprite '{name}' no está declarado")
        return self.sprites[name]
    
    def set_variable(self, name, value):
        self.variables[name] = value
    
    def get_variable(self, name):
        if name not in self.variables:
            raise SemanticError(f"Variable '{name}' no está definida")
        return self.variables[name]


class SemanticAnalyzer:
    """Analizador semántico que recorre el AST"""
    
    # Acciones válidas para sprites
    VALID_ACTIONS = {'move', 'jump', 'run', 'crouch', 'stop', 'set_animation'}
    
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []
    
    def analyze(self, ast):
        """Analiza el AST completo"""
        try:
            self._analyze_program(ast)
            if self.errors:
                raise SemanticError(f"Se encontraron {len(self.errors)} errores:\n" + 
                                  "\n".join(self.errors))
            print("✓ Análisis semántico completado sin errores")
            return True
        except SemanticError as e:
            print(f"✗ Error semántico: {e}")
            return False
    
    def _analyze_program(self, node):
        """Analiza el nodo Program"""
        if not isinstance(node, Program):
            raise SemanticError("El nodo raíz debe ser un Program")
        
        for stmt in node.statements:
            self._analyze_statement(stmt)
    
    def _analyze_statement(self, stmt):
        """Analiza cada tipo de declaración"""
        if isinstance(stmt, SpriteDeclaration):
            self._analyze_sprite_declaration(stmt)
        elif isinstance(stmt, EnvironmentSetting):
            self._analyze_environment_setting(stmt)
        elif isinstance(stmt, ActionNode):
            self._analyze_action(stmt)
        elif isinstance(stmt, IfStatement):
            self._analyze_if_statement(stmt)
        elif isinstance(stmt, LoopStatement):
            self._analyze_loop_statement(stmt)
    
    def _analyze_sprite_declaration(self, node):
        """Valida la declaración de un sprite"""
        x = self._evaluate_expr(node.x)
        y = self._evaluate_expr(node.y)
        
        if not isinstance(x, (int, float)):
            self.errors.append(f"La coordenada X debe ser numérica")
        if not isinstance(y, (int, float)):
            self.errors.append(f"La coordenada Y debe ser numérica")
        
        try:
            self.symbol_table.declare_sprite(node.name, x, y)
        except SemanticError as e:
            self.errors.append(str(e))
    
    def _analyze_environment_setting(self, node):
        """Valida configuraciones del entorno"""
        value = self._evaluate_expr(node.value)
        
        if not isinstance(value, (int, float)):
            self.errors.append(f"El valor de {node.setting_name} debe ser numérico")
        
        self.symbol_table.set_variable(node.setting_name, value)
    
    def _analyze_action(self, node):
        """Valida acciones sobre sprites"""
        # Verificar que el sprite existe
        try:
            self.symbol_table.get_sprite(node.sprite_name)
        except SemanticError as e:
            self.errors.append(str(e))
            return
        
        # Verificar que la acción es válida
        if node.action_type not in self.VALID_ACTIONS:
            self.errors.append(f"Acción inválida: {node.action_type}")
            return
        
        # Validar parámetros según el tipo de acción
        if node.action_type == 'move':
            if len(node.params) != 2:
                self.errors.append(f"move() requiere 2 parámetros (x, y)")
        elif node.action_type == 'run':
            if len(node.params) != 1:
                self.errors.append(f"run() requiere 1 parámetro (speed)")
        elif node.action_type == 'set_animation':
            if len(node.params) != 1:
                self.errors.append(f"set_animation() requiere 1 parámetro (nombre)")
    
    def _analyze_if_statement(self, node):
        """Analiza estructura if"""
        self._evaluate_condition(node.condition)
        for stmt in node.true_block:
            self._analyze_statement(stmt)
        for stmt in node.false_block:
            self._analyze_statement(stmt)
    
    def _analyze_loop_statement(self, node):
        """Analiza estructura loop"""
        iterations = self._evaluate_expr(node.iterations)
        if not isinstance(iterations, (int, float)) or iterations <= 0:
            self.errors.append(f"Las iteraciones del loop deben ser un número positivo")
        
        for stmt in node.body:
            self._analyze_statement(stmt)
    
    def _evaluate_expr(self, expr):
        """Evalúa una expresión y retorna su valor"""
        if isinstance(expr, NumberLiteral):
            return expr.value
        elif isinstance(expr, StringLiteral):
            return expr.value
        elif isinstance(expr, Identifier):
            try:
                return self.symbol_table.get_variable(expr.name)
            except SemanticError:
                return 0  # Valor por defecto
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
        """Evalúa una condición"""
        if isinstance(condition, Condition):
            left = self._evaluate_expr(condition.left)
            right = self._evaluate_expr(condition.right)
            return True
        return True
