# Instalación en Linux - Calculadora Profesional

## 📋 Requisitos Previos

Antes de instalar, asegúrate de tener:
- **Python 3** (versión 3.6 o superior)
- **python3-tk** (biblioteca Tkinter)

### Instalar dependencias en Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3 python3-tk -y
```

### Instalar dependencias en Fedora/RHEL:
```bash
sudo dnf install python3 python3-tkinter -y
```

### Instalar dependencias en Arch Linux:
```bash
sudo pacman -S python tk -y
```

## 🚀 Instalación Automática

### Método 1: Script de Instalación (Recomendado)

1. **Descarga los archivos necesarios:**
   - `calculadora_completa.py`
   - `instalar_linux.sh`
   - `icono.ico` (opcional)

2. **Da permisos de ejecución al instalador:**
   ```bash
   chmod +x instalar_linux.sh
   ```

3. **Ejecuta el instalador:**
   ```bash
   ./instalar_linux.sh
   ```

4. **Sigue las instrucciones en pantalla**

El instalador hará lo siguiente:
- ✅ Verificará las dependencias
- ✅ Copiará los archivos a `~/.local/share/CalculadoraProfesional`
- ✅ Creará un acceso directo en el menú de aplicaciones
- ✅ Opcionalmente creará un acceso directo en el escritorio
- ✅ Creará un desinstalador automático

## 🔧 Instalación Manual

Si prefieres instalar manualmente:

1. **Crear directorio de instalación:**
   ```bash
   mkdir -p ~/.local/share/CalculadoraProfesional
   ```

2. **Copiar archivos:**
   ```bash
   cp calculadora_completa.py ~/.local/share/CalculadoraProfesional/
   cp icono.ico ~/.local/share/CalculadoraProfesional/
   ```

3. **Crear script ejecutable:**
   ```bash
   cat > ~/.local/share/CalculadoraProfesional/calculadora.sh << 'EOF'
   #!/bin/bash
   cd "$(dirname "$0")"
   python3 calculadora_completa.py
   EOF
   
   chmod +x ~/.local/share/CalculadoraProfesional/calculadora.sh
   ```

4. **Crear entrada en el menú de aplicaciones:**
   ```bash
   mkdir -p ~/.local/share/applications
   
   cat > ~/.local/share/applications/calculadora-profesional.desktop << 'EOF'
   [Desktop Entry]
   Version=2.0
   Type=Application
   Name=Calculadora Profesional
   Comment=Calculadora científica con soporte para física
   Exec=$HOME/.local/share/CalculadoraProfesional/calculadora.sh
   Icon=$HOME/.local/share/CalculadoraProfesional/icono.ico
   Terminal=false
   Categories=Utility;Calculator;Science;Education;
   Keywords=calculator;math;science;physics;
   StartupNotify=true
   EOF
   
   chmod +x ~/.local/share/applications/calculadora-profesional.desktop
   ```

5. **Actualizar base de datos de aplicaciones:**
   ```bash
   update-desktop-database ~/.local/share/applications
   ```

## ▶️ Ejecutar la Calculadora

Después de la instalación, puedes ejecutar la calculadora de varias formas:

### Desde el menú de aplicaciones:
- Busca "Calculadora Profesional" en tu menú de aplicaciones

### Desde la terminal:
```bash
~/.local/share/CalculadoraProfesional/calculadora.sh
```

### Desde el escritorio:
- Si creaste el acceso directo, haz doble clic en el icono

## 🗑️ Desinstalar

### Usando el desinstalador automático:
```bash
~/.local/share/CalculadoraProfesional/desinstalar.sh
```

### Desinstalación manual:
```bash
rm -rf ~/.local/share/CalculadoraProfesional
rm -f ~/.local/share/applications/calculadora-profesional.desktop
rm -f ~/Desktop/calculadora-profesional.desktop
rm -f ~/Escritorio/calculadora-profesional.desktop
```

## ✨ Características

- ✅ **Números negativos**: `-5`, `3×(-2)`, `5+(-3)`
- ✅ **Operador de potencia `^`**: `2^3`, `10^2`, `(-2)^3`
- ✅ **Paréntesis**: `(5+3)^2`, `2(3+4)`
- ✅ **Botón ANS**: Reutiliza el resultado anterior
- ✅ **Modo científico**: sin, cos, tan, ln, log, √, x², factorial, etc.
- ✅ **Constantes**: π (pi) y e (euler)
- ✅ **Atajos de teclado**: Todos los operadores funcionan desde el teclado

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'tkinter'"
```bash
# Ubuntu/Debian
sudo apt install python3-tk

# Fedora/RHEL
sudo dnf install python3-tkinter

# Arch Linux
sudo pacman -S tk
```

### El icono no se muestra
- Asegúrate de que el archivo `icono.ico` esté en el directorio de instalación
- Algunos entornos de escritorio pueden tardar en actualizar los iconos
- Intenta cerrar sesión y volver a iniciarla

### La aplicación no aparece en el menú
```bash
update-desktop-database ~/.local/share/applications
```

## 📝 Notas

- La aplicación se instala solo para el usuario actual (no requiere sudo)
- Los archivos se guardan en `~/.local/share/CalculadoraProfesional`
- Compatible con GNOME, KDE, XFCE, y otros entornos de escritorio
- Funciona en Ubuntu, Debian, Fedora, Arch Linux, y otras distribuciones

## 🆘 Soporte

Si tienes problemas con la instalación:
1. Verifica que Python 3 y tkinter estén instalados
2. Asegúrate de tener permisos de escritura en `~/.local/share`
3. Revisa los mensajes de error del instalador
4. Intenta la instalación manual si el script automático falla

---

**¡Disfruta tu calculadora científica en Linux!** 🐧🧮
