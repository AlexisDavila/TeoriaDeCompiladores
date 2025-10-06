# Proyecto: GameScript - Lenguaje para Videojuegos Sencillos
Este repositorio contiene el código fuente para un lenguaje de scripting simple (DSL) diseñado para controlar las acciones de un personaje en un videojuego 2D. El proyecto incluye la gramática formal en ANTLR4 y un driver en Python para probarla.
## Estructura del Repositorio
* GameScript.g4: Archivo de gramática de ANTLR4 que define la sintaxis del lenguaje GameScript.
* driver.py: Programa en Python que lee un archivo de script, lo analiza y muestra las acciones interpretadas.
* test.tf : Un archivo de ejemplo con código escrito en GameScript para probar el driver.
* README.md: Este archivo.
## Requisitos Previos
* Java Development Kit (JDK): ANTLR4 es una herramienta de Java. Necesitas tener Java instalado para generar el parser.
* Python 3: El driver y el runtime de ANTLR4 están en Python.
* ANTLR4 Tool: El archivo .jar para generar el parser. Puedes descargarlo desde el sitio oficial de ANTLR.
* ANTLR4 Python Runtime: La librería de Python necesaria para ejecutar el parser.
## Pasos para la Configuración y Ejecución
1. Instalar el Runtime de ANTLR para Python
Abre tu terminal o consola y ejecuta el siguiente comando:
```
pip install antlr4-python3-runtime
```

2. Generar el Parser desde la Gramática
Coloca el archivo antlr-4.x.x-complete.jar en el mismo directorio del proyecto o configúralo en tu CLASSPATH.
Luego, ejecuta el siguiente comando en la terminal desde la raíz de tu proyecto:

``` 
java -jar antlr-4.x.x-complete.jar -Dlanguage=Python3 GameScript.g4 -visitor
```


Nota: Reemplaza ``` antlr-4.x.x-complete.jar ``` con el nombre exacto de tu archivo. El flag ``` -visitor ``` es importante porque nuestro driver lo utiliza para interpretar el código.

Este comando generará varios archivos nuevos, incluyendo:

```

GameScriptLexer.py
GameScriptParser.py
GameScriptListener.py
GameScriptVisitor.py

```

3. Ejecutar el Driver
Una vez que los archivos del parser han sido generados, puedes probar la gramática ejecutando el ``` driver.py ``` con el script de ejemplo ``` test.tp ```.
python ```driver.py test.tp ```


4. Salida Esperada
Si todo funciona correctamente, deberías ver la siguiente salida en tu consola:
```

Script parsed successfully! Executing actions...
--------------------
Action: MOVE, Direction: right, Steps: 5
Action: JUMP
Action: ATTACK, Target: enemy
Action: WAIT, Duration: 2 seconds
Action: MOVE, Direction: left, Steps: 3
Action: ATTACK, Target: boss
--------------------
Execution finished.

```

Esto demuestra que el driver ha leído, analizado e interpretado correctamente el script sample.gs según las reglas de tu gramática.
