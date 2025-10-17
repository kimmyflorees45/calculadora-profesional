#!/bin/bash

# Script de desinstalación para Calculadora Profesional

set -e

echo "=========================================="
echo "  Desinstalador de Calculadora Profesional  "
echo "=========================================="
echo ""

# Verificar si se ejecuta como root
if [ "$EUID" -eq 0 ]; then 
    echo "⚠️  No ejecutes este script como root (sudo)"
    exit 1
fi

# Definir directorios
INSTALL_DIR="$HOME/.local/share/calculadora-profesional"
BIN_FILE="$HOME/.local/bin/calculadora-profesional"
DESKTOP_FILE="$HOME/.local/share/applications/calculadora-profesional.desktop"
ICON_FILE="$HOME/.local/share/icons/calculadora-profesional.svg"

# Preguntar confirmación
read -p "¿Estás seguro de que deseas desinstalar la Calculadora Profesional? (s/N): " confirmacion

if [[ ! "$confirmacion" =~ ^[sS]$ ]]; then
    echo "Desinstalación cancelada."
    exit 0
fi

echo ""
echo "🗑️  Eliminando archivos..."

# Eliminar archivos
if [ -d "$INSTALL_DIR" ]; then
    rm -rf "$INSTALL_DIR"
    echo "✅ Directorio de instalación eliminado"
fi

if [ -f "$BIN_FILE" ]; then
    rm -f "$BIN_FILE"
    echo "✅ Ejecutable eliminado"
fi

if [ -f "$DESKTOP_FILE" ]; then
    rm -f "$DESKTOP_FILE"
    echo "✅ Acceso directo eliminado"
fi

if [ -f "$ICON_FILE" ]; then
    rm -f "$ICON_FILE"
    echo "✅ Icono eliminado"
fi

# Actualizar base de datos de aplicaciones
if command -v update-desktop-database &> /dev/null; then
    update-desktop-database "$HOME/.local/share/applications" 2>/dev/null || true
fi

echo ""
echo "=========================================="
echo "  ✅ Desinstalación completada  "
echo "=========================================="
echo ""
echo "La Calculadora Profesional ha sido eliminada de tu sistema."
echo ""
