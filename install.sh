#!/bin/bash

# Script de instalación para Calculadora Profesional
# Este script instala la calculadora en Linux

set -e

echo "=========================================="
echo "  Instalador de Calculadora Profesional  "
echo "=========================================="
echo ""

# Verificar si se ejecuta como root
if [ "$EUID" -eq 0 ]; then 
    echo "⚠️  No ejecutes este script como root (sudo)"
    echo "El script pedirá permisos cuando sea necesario"
    exit 1
fi

# Verificar que Python3 y tkinter estén instalados
echo "🔍 Verificando dependencias..."

if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 no está instalado"
    echo "Instálalo con: sudo apt install python3"
    exit 1
fi

# Verificar tkinter
if ! python3 -c "import tkinter" 2>/dev/null; then
    echo "❌ Tkinter no está instalado"
    echo "Instálalo con: sudo apt install python3-tk"
    exit 1
fi

echo "✅ Python3 y Tkinter encontrados"
echo ""

# Definir directorios de instalación
INSTALL_DIR="$HOME/.local/share/calculadora-profesional"
BIN_DIR="$HOME/.local/bin"
DESKTOP_DIR="$HOME/.local/share/applications"
ICON_DIR="$HOME/.local/share/icons"

# Crear directorios si no existen
echo "📁 Creando directorios de instalación..."
mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"
mkdir -p "$DESKTOP_DIR"
mkdir -p "$ICON_DIR"

# Copiar el archivo principal
echo "📋 Copiando archivos..."
cp calculadora_completa.py "$INSTALL_DIR/"
chmod +x "$INSTALL_DIR/calculadora_completa.py"

# Crear script ejecutable en bin
cat > "$BIN_DIR/calculadora-profesional" << 'EOF'
#!/bin/bash
python3 "$HOME/.local/share/calculadora-profesional/calculadora_completa.py"
EOF

chmod +x "$BIN_DIR/calculadora-profesional"

# Crear icono SVG simple
cat > "$ICON_DIR/calculadora-profesional.svg" << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<svg width="128" height="128" viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg">
  <rect width="128" height="128" rx="20" fill="#f5e6f0"/>
  <rect x="16" y="16" width="96" height="96" rx="12" fill="#d4a5d4"/>
  <rect x="24" y="24" width="80" height="24" rx="4" fill="#ffffff"/>
  <text x="64" y="42" font-family="Arial" font-size="16" font-weight="bold" fill="#7b4b94" text-anchor="middle">123</text>
  <g fill="#f4a6d7">
    <rect x="24" y="56" width="18" height="14" rx="2"/>
    <rect x="46" y="56" width="18" height="14" rx="2"/>
    <rect x="68" y="56" width="18" height="14" rx="2"/>
    <rect x="90" y="56" width="14" height="14" rx="2"/>
    <rect x="24" y="74" width="18" height="14" rx="2"/>
    <rect x="46" y="74" width="18" height="14" rx="2"/>
    <rect x="68" y="74" width="18" height="14" rx="2"/>
    <rect x="90" y="74" width="14" height="14" rx="2"/>
    <rect x="24" y="92" width="18" height="14" rx="2"/>
    <rect x="46" y="92" width="18" height="14" rx="2"/>
    <rect x="68" y="92" width="18" height="14" rx="2"/>
    <rect x="90" y="92" width="14" height="14" rx="2"/>
  </g>
</svg>
EOF

# Crear archivo .desktop
cat > "$DESKTOP_DIR/calculadora-profesional.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Calculadora Profesional
Comment=Calculadora científica con juego de divisiones
Exec=$BIN_DIR/calculadora-profesional
Icon=$ICON_DIR/calculadora-profesional.svg
Terminal=false
Categories=Utility;Calculator;Education;
Keywords=calculator;math;science;division;game;
StartupNotify=true
EOF

chmod +x "$DESKTOP_DIR/calculadora-profesional.desktop"

# Actualizar base de datos de aplicaciones
if command -v update-desktop-database &> /dev/null; then
    update-desktop-database "$DESKTOP_DIR" 2>/dev/null || true
fi

echo ""
echo "=========================================="
echo "  ✅ Instalación completada exitosamente  "
echo "=========================================="
echo ""
echo "📍 Ubicación de archivos:"
echo "   • Programa: $INSTALL_DIR/calculadora_completa.py"
echo "   • Ejecutable: $BIN_DIR/calculadora-profesional"
echo "   • Icono: $ICON_DIR/calculadora-profesional.svg"
echo "   • Acceso directo: $DESKTOP_DIR/calculadora-profesional.desktop"
echo ""
echo "🚀 Formas de ejecutar la calculadora:"
echo "   1. Desde el menú de aplicaciones (busca 'Calculadora Profesional')"
echo "   2. Desde la terminal: calculadora-profesional"
echo "   3. Directamente: python3 $INSTALL_DIR/calculadora_completa.py"
echo ""
echo "💡 Nota: Si el comando 'calculadora-profesional' no funciona,"
echo "   asegúrate de que $BIN_DIR esté en tu PATH."
echo "   Puedes agregarlo con:"
echo "   echo 'export PATH=\"\$HOME/.local/bin:\$PATH\"' >> ~/.bashrc"
echo "   source ~/.bashrc"
echo ""
echo "🗑️  Para desinstalar, ejecuta: ./uninstall.sh"
echo ""
