#!/bin/bash

# Script de instalación para Calculadora Profesional en macOS
# Autor: Tu Nombre
# Versión: 2.0

# Colores para la terminal
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # Sin color

clear
echo -e "${BLUE}=========================================="
echo -e "  INSTALADOR - CALCULADORA PROFESIONAL"
echo -e "  macOS"
echo -e "==========================================${NC}"
echo ""
echo -e "${YELLOW}Este script instalará la calculadora en tu Mac${NC}"
echo ""
read -p "Presiona ENTER para continuar o Ctrl+C para cancelar..."

# Verificar que Python3 y tkinter estén instalados
echo ""
echo -e "${BLUE}[1/6] Verificando Python3...${NC}"

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}✗ Python3 no está instalado${NC}"
    echo ""
    echo "Por favor instala Python3 primero:"
    echo "  1. Ve a https://www.python.org/downloads/"
    echo "  2. Descarga Python 3 para macOS"
    echo "  3. Instala y vuelve a ejecutar este script"
    echo ""
    echo "O instala con Homebrew:"
    echo "  brew install python-tk@3.11"
    exit 1
fi
echo -e "${GREEN}✓ Python3 encontrado${NC}"

# Verificar tkinter
echo -e "${BLUE}[2/6] Verificando tkinter...${NC}"
if ! python3 -c "import tkinter" 2>/dev/null; then
    echo -e "${YELLOW}⚠ tkinter no está instalado${NC}"
    echo ""
    echo "Instalando tkinter con Homebrew..."
    
    # Verificar si Homebrew está instalado
    if ! command -v brew &> /dev/null; then
        echo -e "${YELLOW}Homebrew no está instalado. Instalando...${NC}"
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    
    # Instalar python-tk
    brew install python-tk@3.11
    
    # Verificar de nuevo
    if ! python3 -c "import tkinter" 2>/dev/null; then
        echo -e "${RED}✗ No se pudo instalar tkinter${NC}"
        echo "Instala Python desde python.org que incluye tkinter"
        exit 1
    fi
fi
echo -e "${GREEN}✓ tkinter disponible${NC}"

# Crear directorios
echo -e "${BLUE}[3/6] Creando directorios...${NC}"
INSTALL_DIR="$HOME/Library/Application Support/CalculadoraProfesional"
APP_DIR="$HOME/Applications"

mkdir -p "$INSTALL_DIR"
mkdir -p "$APP_DIR"
echo -e "${GREEN}✓ Directorios creados${NC}"

# Copiar archivos
echo -e "${BLUE}[4/6] Instalando aplicación...${NC}"

if [ -f "calculadora_completa.py" ]; then
    cp calculadora_completa.py "$INSTALL_DIR/"
    echo -e "${GREEN}✓ Archivo copiado${NC}"
else
    echo -e "${RED}✗ Archivo calculadora_completa.py no encontrado${NC}"
    exit 1
fi

# Copiar icono si existe
if [ -f "icono.ico" ]; then
    cp icono.ico "$INSTALL_DIR/"
fi

# Crear script ejecutable
echo -e "${BLUE}[5/6] Configurando ejecutable...${NC}"
cat > "$INSTALL_DIR/calculadora.command" << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
python3 calculadora_completa.py
EOF

chmod +x "$INSTALL_DIR/calculadora.command"

# Crear alias en Applications
ln -sf "$INSTALL_DIR/calculadora.command" "$APP_DIR/Calculadora Profesional.command"

echo -e "${GREEN}✓ Ejecutable configurado${NC}"

# Crear aplicación .app (opcional, más nativo)
echo -e "${BLUE}[6/6] Creando aplicación nativa...${NC}"
APP_PATH="$APP_DIR/Calculadora Profesional.app"
mkdir -p "$APP_PATH/Contents/MacOS"
mkdir -p "$APP_PATH/Contents/Resources"

# Crear Info.plist
cat > "$APP_PATH/Contents/Info.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>Calculadora Profesional</string>
    <key>CFBundleIdentifier</key>
    <string>com.calculadora.profesional</string>
    <key>CFBundleName</key>
    <string>Calculadora Profesional</string>
    <key>CFBundleVersion</key>
    <string>2.0</string>
    <key>CFBundleShortVersionString</key>
    <string>2.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.13</string>
</dict>
</plist>
EOF

# Crear script launcher
cat > "$APP_PATH/Contents/MacOS/Calculadora Profesional" << EOF
#!/bin/bash
cd "$INSTALL_DIR"
python3 calculadora_completa.py
EOF

chmod +x "$APP_PATH/Contents/MacOS/Calculadora Profesional"

echo -e "${GREEN}✓ Aplicación nativa creada${NC}"

# Crear desinstalador
cat > "$INSTALL_DIR/desinstalar.command" << 'UNINSTALL_EOF'
#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

clear
echo -e "${RED}=========================================="
echo -e "  DESINSTALADOR - CALCULADORA PROFESIONAL"
echo -e "==========================================${NC}"
echo ""
echo -e "${BLUE}Esto eliminará:${NC}"
echo "  - La aplicación instalada"
echo "  - Los accesos directos"
echo ""
read -p "¿Estás seguro? (s/n): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[SsYy]$ ]]; then
    echo ""
    echo -e "${BLUE}Eliminando archivos...${NC}"
    
    # Eliminar aplicación
    rm -rf "$HOME/Library/Application Support/CalculadoraProfesional"
    rm -f "$HOME/Applications/Calculadora Profesional.command"
    rm -rf "$HOME/Applications/Calculadora Profesional.app"
    
    echo ""
    echo -e "${GREEN}=========================================="
    echo -e "  DESINSTALACIÓN COMPLETADA"
    echo -e "==========================================${NC}"
    echo ""
else
    echo ""
    echo "Desinstalación cancelada."
    echo ""
fi
UNINSTALL_EOF

chmod +x "$INSTALL_DIR/desinstalar.command"

echo ""
echo -e "${GREEN}=========================================="
echo -e "  ✓ INSTALACIÓN COMPLETADA"
echo -e "==========================================${NC}"
echo ""
echo -e "${YELLOW}La calculadora ha sido instalada en:${NC}"
echo "  $INSTALL_DIR"
echo ""
echo -e "${YELLOW}Puedes encontrarla en:${NC}"
echo "  • Carpeta Aplicaciones (~/Applications)"
echo "  • Busca 'Calculadora Profesional'"
echo ""
echo -e "${YELLOW}Para ejecutar desde terminal:${NC}"
echo "  open '$APP_PATH'"
echo ""
echo -e "${YELLOW}Para desinstalar:${NC}"
echo "  $INSTALL_DIR/desinstalar.command"
echo ""
echo -e "${GREEN}¡Disfruta tu calculadora científica!${NC} 🧮"
echo ""
