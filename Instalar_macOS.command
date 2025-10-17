#!/bin/bash
# Instalador Automático para macOS
# Solo haz doble clic en este archivo

echo "🧮 Instalando Calculadora Profesional..."
echo ""

# Obtener el directorio del script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Verificar Python 3
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado"
    echo "Instálalo desde: https://www.python.org/downloads/"
    read -p "Presiona Enter para salir..."
    exit 1
fi

echo "✅ Python 3 encontrado"

# Verificar Tkinter
if ! python3 -c "import tkinter" &> /dev/null; then
    echo "❌ Tkinter no está disponible"
    echo "Instala con: brew install python-tk"
    read -p "Presiona Enter para salir..."
    exit 1
fi

echo "✅ Tkinter encontrado"
echo ""
echo "🚀 Iniciando Calculadora..."
echo ""

# Ejecutar la calculadora
cd "$DIR"
python3 calculadora.py

echo ""
echo "✅ Calculadora cerrada"
read -p "Presiona Enter para salir..."
