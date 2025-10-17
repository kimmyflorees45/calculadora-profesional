#!/bin/bash
# Calculadora Profesional para macOS
# Doble clic para ejecutar

# Obtener el directorio del script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Ejecutar la calculadora
cd "$DIR"
python3 calculadora.py 2>/dev/null

# Si falla, mostrar mensaje de error
if [ $? -ne 0 ]; then
    osascript -e 'display dialog "Error: Python 3 no está instalado.\n\nInstálalo desde:\nhttps://www.python.org/downloads/" buttons {"OK"} default button 1 with icon stop'
fi
