#!/bin/bash

# Script de compilación para Mini2DLang
# Este script automatiza todo el proceso de configuración

echo "=================================================="
echo "  COMPILADOR MINI2DLANG - SCRIPT DE INSTALACIÓN"
echo "=================================================="

# 1. Instalar dependencias de Python
echo ""
echo "[1/4] Instalando dependencias de Python..."
pip install antlr4-python3-runtime pygame

# 2. Descargar ANTLR si no existe
if [ ! -f "antlr-4.13.1-complete.jar" ]; then
    echo ""
    echo "[2/4] Descargando ANTLR 4.13.1..."
    curl -O https://www.antlr.org/download/antlr-4.13.1-complete.jar
else
    echo ""
    echo "[2/4] ANTLR 4.13.1 ya está descargado"
fi

# 3. Crear directorios si no existen
echo ""
echo "[3/4] Creando estructura de directorios..."
mkdir -p grammar
mkdir -p compiler
mkdir -p engine

# 4. Compilar gramáticas
echo ""
echo "[4/4] Compilando gramáticas ANTLR..."
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -o grammar grammar/Mini2DLangLexer.g4
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -o grammar grammar/Mini2DLangParser.g4

echo ""
echo "=================================================="
echo "  ✓ INSTALACIÓN COMPLETADA"
echo "=================================================="
echo ""
echo "Para ejecutar el compilador, usa:"
echo "  python main.py example_script.m2d"
echo ""
