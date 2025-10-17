#!/bin/bash

# Script de instalación para Calculadora Profesional en Linux
# Autor: Tu Nombre
# Versión: 2.0

# Colores para la terminal
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # Sin color

clear
echo -e "${BLUE}========================================"
echo -e "  INSTALADOR - CALCULADORA PROFESIONAL"
echo -e "========================================${NC}"
echo ""
echo -e "${YELLOW}Este instalador copiará la calculadora a:${NC}"
echo -e "  ~/.local/share/CalculadoraProfesional"
echo ""
echo -e "${YELLOW}Y creará accesos directos en:${NC}"
echo -e "  - Menú de aplicaciones"
echo -e "  - Escritorio (opcional)"
echo ""
read -p "Presiona ENTER para continuar o Ctrl+C para cancelar..."

# Verificar que Python3 y tkinter estén instalados
echo ""
echo -e "${BLUE}Verificando dependencias...${NC}"

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python3 no está instalado.${NC}"
    echo "Instálalo con: sudo apt install python3 python3-tk"
    exit 1
fi

if ! python3 -c "import tkinter" 2>/dev/null; then
    echo -e "${YELLOW}Advertencia: tkinter no está instalado.${NC}"
    echo "Instalando tkinter..."
    sudo apt install python3-tk -y
fi

echo -e "${GREEN}✓ Dependencias verificadas${NC}"

# Crear directorios
INSTALL_DIR="$HOME/.local/share/CalculadoraProfesional"
DESKTOP_DIR="$HOME/.local/share/applications"
ICON_DIR="$HOME/.local/share/icons"

echo ""
echo -e "${BLUE}Creando directorios...${NC}"
mkdir -p "$INSTALL_DIR"
mkdir -p "$DESKTOP_DIR"
mkdir -p "$ICON_DIR"

# Copiar archivos
echo -e "${BLUE}Copiando archivos...${NC}"
cp calculadora_completa.py "$INSTALL_DIR/"
if [ -f "icono.ico" ]; then
    cp icono.ico "$INSTALL_DIR/"
fi

# Crear script ejecutable
echo -e "${BLUE}Creando ejecutable...${NC}"
cat > "$INSTALL_DIR/calculadora.sh" << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
python3 calculadora_completa.py
EOF

chmod +x "$INSTALL_DIR/calculadora.sh"

# Crear archivo .desktop para el menú de aplicaciones
echo -e "${BLUE}Creando entrada en el menú de aplicaciones...${NC}"
cat > "$DESKTOP_DIR/calculadora-profesional.desktop" << EOF
[Desktop Entry]
Version=2.0
Type=Application
Name=Calculadora Profesional
Comment=Calculadora científica con soporte para física
Exec=$INSTALL_DIR/calculadora.sh
Icon=$INSTALL_DIR/icono.ico
Terminal=false
Categories=Utility;Calculator;Science;Education;
Keywords=calculator;math;science;physics;
StartupNotify=true
EOF

chmod +x "$DESKTOP_DIR/calculadora-profesional.desktop"

# Preguntar si crear acceso directo en el escritorio
echo ""
read -p "¿Deseas crear un acceso directo en el escritorio? (s/n): " -n 1 -r
echo ""
if [[ $REPLY =~ ^[SsYy]$ ]]; then
    DESKTOP_PATH="$HOME/Desktop"
    if [ ! -d "$DESKTOP_PATH" ]; then
        DESKTOP_PATH="$HOME/Escritorio"
    fi
    
    if [ -d "$DESKTOP_PATH" ]; then
        cp "$DESKTOP_DIR/calculadora-profesional.desktop" "$DESKTOP_PATH/"
        chmod +x "$DESKTOP_PATH/calculadora-profesional.desktop"
        # Marcar como confiable en GNOME
        gio set "$DESKTOP_PATH/calculadora-profesional.desktop" metadata::trusted true 2>/dev/null
        echo -e "${GREEN}✓ Acceso directo creado en el escritorio${NC}"
    else
        echo -e "${YELLOW}No se pudo encontrar el directorio del escritorio${NC}"
    fi
fi

# Crear desinstalador
echo -e "${BLUE}Creando desinstalador...${NC}"
cat > "$INSTALL_DIR/desinstalar.sh" << 'UNINSTALL_EOF'
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
    
    # Eliminar accesos directos
    rm -f "$HOME/.local/share/applications/calculadora-profesional.desktop"
    rm -f "$HOME/Desktop/calculadora-profesional.desktop"
    rm -f "$HOME/Escritorio/calculadora-profesional.desktop"
    
    # Eliminar directorio de instalación
    rm -rf "$HOME/.local/share/CalculadoraProfesional"
    
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

chmod +x "$INSTALL_DIR/desinstalar.sh"

# Actualizar base de datos de aplicaciones
update-desktop-database "$DESKTOP_DIR" 2>/dev/null

echo ""
echo -e "${GREEN}=========================================="
echo -e "  INSTALACIÓN COMPLETADA EXITOSAMENTE"
echo -e "==========================================${NC}"
echo ""
echo -e "${YELLOW}La calculadora ha sido instalada en:${NC}"
echo "  $INSTALL_DIR"
echo ""
echo -e "${YELLOW}Puedes encontrarla en:${NC}"
echo "  - Menú de aplicaciones (busca 'Calculadora Profesional')"
echo "  - Escritorio (si elegiste crear el acceso directo)"
echo ""
echo -e "${YELLOW}Para desinstalar, ejecuta:${NC}"
echo "  $INSTALL_DIR/desinstalar.sh"
echo ""
echo -e "${GREEN}¡Disfruta tu calculadora científica!${NC} 🧮"
echo ""
