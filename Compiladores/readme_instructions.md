# Compilador Mini2DLang

## Descripción

Mini2DLang es un lenguaje de dominio específico (DSL) para controlar sprites en un motor 2D. Este proyecto implementa un compilador completo que incluye:

- **Análisis Léxico** (Lexer) con ANTLR 4.13.1
- **Análisis Sintáctico** (Parser) con ANTLR 4.13.1
- **Árbol de Sintaxis Abstracta** (AST)
- **Análisis Semántico**
- **Intérprete**
- **Motor 2D** con Pygame

## Estructura del Proyecto

```
mini2dlang-compiler/
├── grammar/
│   ├── Mini2DLangLexer.g4       # Gramática del lexer
│   └── Mini2DLangParser.g4      # Gramática del parser
├── compiler/
│   ├── ast_nodes.py             # Nodos del AST
│   ├── semantic_analyzer.py     # Analizador semántico
│   └── interpreter.py           # Intérprete
├── engine/
│   ├── sprite_object.py         # Clase Sprite
│   └── game_driver.py           # Motor del juego
├── main.py                      # Punto de entrada
├── example_script.m2d           # Script de ejemplo
└── README.md                    # Este archivo
```

## Instalación

### 1. Instalar dependencias de Python

```bash
pip install antlr4-python3-runtime pygame
```

### 2. Descargar ANTLR 4.13.1

```bash
curl -O https://www.antlr.org/download/antlr-4.13.1-complete.jar
```

### 3. Compilar las gramáticas

```bash
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -o grammar grammar/Mini2DLangLexer.g4 grammar/Mini2DLangParser.g4
```

## Uso

### Ejecutar el script de ejemplo

```bash
python main.py example_script.m2d
```

### Ejecutar un script personalizado

```bash
python main.py mi_script.m2d
```

## Sintaxis del Lenguaje

### 1. Configuración del Entorno

```
set gravity = 0.8
set world_width = 800
set world_height = 600
set player_speed = 5
```

### 2. Declaración de Sprites

```
sprite player at (100, 200)
sprite enemy at (600, 300)
```

### 3. Acciones de Sprites

```
player.move(10, 5)           // Mover por dx, dy
player.jump()                // Saltar
player.run(8)                // Correr a velocidad
player.crouch()              // Agacharse
player.stop()                // Detenerse
player.set_animation("idle") // Cambiar animación
```

### 4. Control de Flujo

```
// Bucle
loop 10 {
    player.move(5, 0)
}

// Condicional (sintaxis básica)
if x > 100 {
    player.jump()
} else {
    player.stop()
}
```

### 5. Comentarios

```
// Comentario de una línea

/* Comentario
   multilínea */
```

## Ejemplo Completo

```
// Configurar el mundo
set gravity = 0.8
set world_width = 800
set world_height = 600

// Crear personaje
sprite hero at (100, 400)

// Secuencia de acciones
hero.set_animation("running")
hero.run(10)

loop 5 {
    hero.move(15, 0)
}

hero.jump()
hero.stop()
```

## Fases de Compilación

### 1. Análisis Léxico
El lexer tokeniza el código fuente en tokens como:
- Palabras reservadas: `sprite`, `move`, `jump`, etc.
- Identificadores: nombres de sprites
- Números y strings
- Operadores y delimitadores

### 2. Análisis Sintáctico
El parser construye un árbol de sintaxis concreta verificando que la estructura del código sea válida.

### 3. Construcción del AST
Se convierte el árbol de sintaxis concreta en un AST simplificado con nodos como:
- `Program`
- `SpriteDeclaration`
- `ActionNode`
- `IfStatement`
- `LoopStatement`

### 4. Análisis Semántico
Verifica:
- Sprites declarados antes de usarse
- Parámetros correctos en cada acción
- Tipos de datos válidos
- Variables definidas

### 5. Interpretación
El intérprete recorre el AST y ejecuta comandos en el motor 2D.

### 6. Ejecución
El motor Pygame renderiza los sprites y aplica física básica (gravedad, colisiones).

## Motor 2D

### Características

- **Física básica**: Gravedad, velocidad, colisiones con el suelo
- **Animaciones**: Estados visuales (idle, running, jumping, crouching)
- **Renderizado**: Sprites representados como rectángulos de colores
- **Game Loop**: 60 FPS

### Controles

- **ESC**: Salir del juego
- **SPACE**: Pausar (funcionalidad futura)

## Salida del Compilador

Al ejecutar un script, verás:

```
============================================================
COMPILADOR MINI2DLANG
============================================================

[1/6] Cargando script: example_script.m2d
✓ Script cargado (X caracteres)

[2/6] Análisis Léxico (Lexer)
✓ Se encontraron X tokens

[3/6] Análisis Sintáctico (Parser)
✓ Árbol de sintaxis concreta generado

[4/6] Construcción del AST
✓ AST construido con X declaraciones

[5/6] Análisis Semántico
✓ Análisis semántico completado sin errores

[6/6] Interpretación y Ejecución
=== Iniciando interpretación ===
  Configurando gravity = 0.8
  Creando sprite 'player' en (100, 400)
  ...
=== Interpretación completada ===

⚡ Iniciando motor 2D...
```

## Extensiones Futuras

- [ ] Variables y expresiones aritméticas complejas
- [ ] Funciones definidas por el usuario
- [ ] Detección de colisiones entre sprites
- [ ] Texturas e imágenes reales
- [ ] Sonidos y música
- [ ] Sistema de partículas
- [ ] Físicas más avanzadas

## Autor

Proyecto educativo - Compilador Mini2DLang

## Licencia

Uso educativo libre
