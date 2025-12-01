"""
Nodos del AST para Mini2DLang
Cada nodo representa un elemento sintáctico del lenguaje
"""

class ASTNode:
    """Clase base para todos los nodos del AST"""
    pass


class Program(ASTNode):
    """Nodo raíz que contiene todas las declaraciones"""
    def __init__(self, statements):
        self.statements = statements
    
    def __repr__(self):
        return f"Program({len(self.statements)} statements)"


class SpriteDeclaration(ASTNode):
    """Declaración de un sprite: sprite player at (100, 200)"""
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"SpriteDeclaration(name={self.name}, x={self.x}, y={self.y})"


class EnvironmentSetting(ASTNode):
    """Configuración del entorno: set gravity = 0.8"""
    def __init__(self, setting_name, value):
        self.setting_name = setting_name
        self.value = value
    
    def __repr__(self):
        return f"EnvironmentSetting({self.setting_name}={self.value})"


class ActionNode(ASTNode):
    """Acción sobre un sprite"""
    def __init__(self, sprite_name, action_type, params=None):
        self.sprite_name = sprite_name
        self.action_type = action_type
        self.params = params or []
    
    def __repr__(self):
        return f"ActionNode({self.sprite_name}.{self.action_type}({self.params}))"


class IfStatement(ASTNode):
    """Estructura de control if/else"""
    def __init__(self, condition, true_block, false_block=None):
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block or []
    
    def __repr__(self):
        return f"IfStatement(condition={self.condition})"


class LoopStatement(ASTNode):
    """Estructura de bucle: loop 10 { }"""
    def __init__(self, iterations, body):
        self.iterations = iterations
        self.body = body
    
    def __repr__(self):
        return f"LoopStatement(iterations={self.iterations})"


class Condition(ASTNode):
    """Condición para control de flujo"""
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
    
    def __repr__(self):
        return f"Condition({self.left} {self.operator} {self.right})"


class BinaryOp(ASTNode):
    """Operación binaria: +, -, *, /"""
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
    
    def __repr__(self):
        return f"BinaryOp({self.left} {self.operator} {self.right})"


class NumberLiteral(ASTNode):
    """Literal numérico"""
    def __init__(self, value):
        self.value = float(value)
    
    def __repr__(self):
        return f"Number({self.value})"


class StringLiteral(ASTNode):
    """Literal de cadena"""
    def __init__(self, value):
        self.value = value.strip('"')
    
    def __repr__(self):
        return f"String('{self.value}')"


class Identifier(ASTNode):
    """Identificador de variable"""
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Identifier({self.name})"
