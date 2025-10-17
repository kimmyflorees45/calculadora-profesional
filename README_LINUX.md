# 🧮 Calculadora Profesional - Instalación en Linux

Una calculadora moderna con interfaz gráfica que incluye modo científico y un juego educativo de divisiones.

## 📋 Requisitos Previos

Antes de instalar, asegúrate de tener instalado:

- **Python 3** (versión 3.6 o superior)
- **Tkinter** (interfaz gráfica para Python)

### Verificar si tienes Python 3:
```bash
python3 --version
```

### Instalar dependencias en Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3 python3-tk
```

### Instalar dependencias en Fedora/RHEL:
```bash
sudo dnf install python3 python3-tkinter
```

### Instalar dependencias en Arch Linux:
```bash
sudo pacman -S python tk
```

## 🚀 Instalación Rápida

1. **Descarga o copia los archivos** a una carpeta en tu sistema Linux

2. **Abre una terminal** en la carpeta donde están los archivos

3. **Da permisos de ejecución** al instalador:
   ```bash
   chmod +x install.sh
   ```

4. **Ejecuta el instalador**:
   ```bash
   ./install.sh
   ```

¡Listo! La calculadora estará instalada en tu sistema.

## 📂 Archivos Necesarios

Para la instalación necesitas estos archivos:
- `calculadora_completa.py` - El programa principal
- `install.sh` - Script de instalación
- `uninstall.sh` - Script de desinstalación (opcional)
- `README_LINUX.md` - Este archivo (opcional)

## 🎯 Cómo Usar la Calculadora

Después de la instalación, puedes abrir la calculadora de 3 formas:

### 1. Desde el Menú de Aplicaciones
- Busca "Calculadora Profesional" en tu menú de aplicaciones
- Haz clic en el icono para abrirla

### 2. Desde la Terminal
```bash
calculadora-profesional
```

### 3. Directamente con Python
```bash
python3 ~/.local/share/calculadora-profesional/calculadora_completa.py
```

## ✨ Características

### Modo Básico
- ✅ Operaciones aritméticas básicas (+, -, ×, ÷)
- ✅ Porcentajes (%)
- ✅ Cambio de signo (±)
- ✅ Interfaz moderna y colorida
- ✅ Atajos de teclado

### Modo Científico
- 🔬 Funciones trigonométricas (sin, cos, tan)
- 🔬 Logaritmos (ln, log)
- 🔬 Raíz cuadrada (√)
- 🔬 Potencias (x², xʸ)
- 🔬 Factorial (x!)
- 🔬 Inverso (1/x)
- 🔬 Constantes matemáticas (π, e)
- 🔬 Paréntesis para expresiones complejas
- 🔬 Memoria de resultado anterior (ANS)

### Juego de Divisiones
- 🎮 Aprende divisiones de forma divertida
- 🎮 Sistema de niveles progresivos
- 🎮 Puntuación y feedback visual
- 🎮 Calculadora integrada para ayuda
- 🎮 Explicaciones paso a paso

## ⌨️ Atajos de Teclado

- **Enter** - Calcular resultado (=)
- **Backspace** - Borrar último carácter (⌫)
- **Escape** - Limpiar todo (C)
- **0-9** - Números
- **+, -, *, /** - Operadores
- **.** - Punto decimal
- **(, )** - Paréntesis

## 📍 Ubicación de Archivos Instalados

Después de la instalación, los archivos estarán en:

```
~/.local/share/calculadora-profesional/    # Programa principal
~/.local/bin/calculadora-profesional        # Ejecutable
~/.local/share/applications/                # Acceso directo
~/.local/share/icons/                       # Icono
```

## 🔧 Solución de Problemas

### El comando 'calculadora-profesional' no funciona

Si después de instalar no puedes ejecutar el comando desde la terminal, necesitas agregar `~/.local/bin` a tu PATH:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Para **Zsh** (si usas Oh My Zsh):
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Error: "tkinter module not found"

Instala el paquete tkinter:
```bash
# Ubuntu/Debian
sudo apt install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch
sudo pacman -S tk
```

### La aplicación no aparece en el menú

Espera unos segundos y actualiza el menú, o cierra sesión y vuelve a entrar. También puedes forzar la actualización:

```bash
update-desktop-database ~/.local/share/applications/
```

### Problemas con permisos

Asegúrate de NO ejecutar el instalador con `sudo`. El script está diseñado para instalarse en tu directorio personal sin necesidad de permisos de administrador.

## 🗑️ Desinstalación

Para desinstalar la calculadora:

1. **Da permisos de ejecución** al desinstalador:
   ```bash
   chmod +x uninstall.sh
   ```

2. **Ejecuta el desinstalador**:
   ```bash
   ./uninstall.sh
   ```

O manualmente:
```bash
rm -rf ~/.local/share/calculadora-profesional
rm -f ~/.local/bin/calculadora-profesional
rm -f ~/.local/share/applications/calculadora-profesional.desktop
rm -f ~/.local/share/icons/calculadora-profesional.svg
```

## 🎨 Personalización

El código fuente está en `~/.local/share/calculadora-profesional/calculadora_completa.py`. Puedes editarlo para personalizar:
- Colores de la interfaz
- Tamaños de fuente
- Funciones adicionales
- Niveles del juego

Después de editar, los cambios se aplicarán la próxima vez que abras la calculadora.

## 📝 Notas Adicionales

- La calculadora usa **grados** para funciones trigonométricas (no radianes)
- Los resultados se redondean automáticamente para mejor legibilidad
- El juego de divisiones guarda el progreso durante la sesión actual
- La interfaz se adapta al tamaño de la ventana

## 🐛 Reportar Problemas

Si encuentras algún error o tienes sugerencias, por favor repórtalo con:
- Versión de Python (`python3 --version`)
- Distribución de Linux (`cat /etc/os-release`)
- Descripción del problema
- Mensaje de error (si hay alguno)

## 📄 Licencia

Este software es de uso libre para fines educativos y personales.

---

**¡Disfruta tu Calculadora Profesional! 🎉**
