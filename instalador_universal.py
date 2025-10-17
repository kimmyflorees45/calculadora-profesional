#!/usr/bin/env python3
"""
Instalador Universal - Calculadora Profesional
Detecta automáticamente el sistema operativo e instala la aplicación
"""

import os
import sys
import platform
import shutil
import subprocess
from pathlib import Path

# Colores para terminal
class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header():
    """Mostrar encabezado"""
    print(f"\n{Colors.BLUE}{Colors.BOLD}{'='*50}")
    print("  INSTALADOR UNIVERSAL")
    print("  CALCULADORA PROFESIONAL v2.0")
    print(f"{'='*50}{Colors.END}\n")

def print_success(msg):
    print(f"{Colors.GREEN}✓ {msg}{Colors.END}")

def print_error(msg):
    print(f"{Colors.RED}✗ {msg}{Colors.END}")

def print_info(msg):
    print(f"{Colors.BLUE}→ {msg}{Colors.END}")

def print_warning(msg):
    print(f"{Colors.YELLOW}⚠ {msg}{Colors.END}")

def detect_os():
    """Detectar sistema operativo"""
    system = platform.system()
    if system == "Windows":
        return "windows"
    elif system == "Linux":
        return "linux"
    elif system == "Darwin":
        return "mac"
    else:
        return "unknown"

def check_python_version():
    """Verificar versión de Python"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        print_error("Se requiere Python 3.6 o superior")
        return False
    print_success(f"Python {version.major}.{version.minor}.{version.micro}")
    return True

def check_tkinter():
    """Verificar que tkinter esté instalado"""
    try:
        import tkinter
        print_success("tkinter disponible")
        return True
    except ImportError:
        print_warning("tkinter no está instalado")
        return False

def install_tkinter_linux():
    """Intentar instalar tkinter en Linux"""
    print_info("Intentando instalar tkinter...")
    
    # Detectar distribución
    try:
        with open('/etc/os-release', 'r') as f:
            os_info = f.read().lower()
        
        if 'ubuntu' in os_info or 'debian' in os_info:
            cmd = ['sudo', 'apt', 'install', '-y', 'python3-tk']
        elif 'fedora' in os_info or 'rhel' in os_info:
            cmd = ['sudo', 'dnf', 'install', '-y', 'python3-tkinter']
        elif 'arch' in os_info:
            cmd = ['sudo', 'pacman', '-S', '--noconfirm', 'tk']
        else:
            print_error("Distribución no reconocida")
            print_info("Instala tkinter manualmente:")
            print("  Ubuntu/Debian: sudo apt install python3-tk")
            print("  Fedora: sudo dnf install python3-tkinter")
            print("  Arch: sudo pacman -S tk")
            return False
        
        subprocess.run(cmd, check=True)
        print_success("tkinter instalado")
        return True
    except Exception as e:
        print_error(f"No se pudo instalar tkinter: {e}")
        return False

def install_windows():
    """Instalar en Windows"""
    print_info("Instalando en Windows...")
    
    # Directorio de instalación
    install_dir = Path(os.environ['LOCALAPPDATA']) / 'CalculadoraProfesional'
    install_dir.mkdir(parents=True, exist_ok=True)
    
    # Copiar archivos
    print_info("Copiando archivos...")
    script_dir = Path(__file__).parent
    
    # Código de la calculadora embebido
    calc_code = (script_dir / 'calculadora_completa.py').read_text(encoding='utf-8')
    (install_dir / 'calculadora_completa.py').write_text(calc_code, encoding='utf-8')
    
    # Copiar icono si existe
    if (script_dir / 'icono.ico').exists():
        shutil.copy(script_dir / 'icono.ico', install_dir / 'icono.ico')
    
    print_success("Archivos copiados")
    
    # Crear script de ejecución
    print_info("Creando ejecutable...")
    launcher = install_dir / 'calculadora.bat'
    launcher.write_text(f'@echo off\npython "{install_dir / "calculadora_completa.py"}"', encoding='utf-8')
    
    # Crear acceso directo en el escritorio
    print_info("Creando accesos directos...")
    try:
        import winshell
        from win32com.client import Dispatch
        
        desktop = winshell.desktop()
        shortcut_path = Path(desktop) / 'Calculadora Profesional.lnk'
        
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(str(shortcut_path))
        shortcut.Targetpath = sys.executable
        shortcut.Arguments = f'"{install_dir / "calculadora_completa.py"}"'
        shortcut.WorkingDirectory = str(install_dir)
        if (install_dir / 'icono.ico').exists():
            shortcut.IconLocation = str(install_dir / 'icono.ico')
        shortcut.save()
        
        print_success("Acceso directo creado en el escritorio")
    except ImportError:
        print_warning("No se pudo crear acceso directo (requiere pywin32)")
        print_info(f"Ejecuta manualmente: {launcher}")
    
    # Crear desinstalador
    uninstaller = install_dir / 'desinstalar.bat'
    uninstaller.write_text(f'''@echo off
echo Desinstalando Calculadora Profesional...
rd /s /q "{install_dir}"
del "%USERPROFILE%\\Desktop\\Calculadora Profesional.lnk" 2>nul
echo Desinstalacion completada
pause
''', encoding='utf-8')
    
    print_success(f"Instalación completada en: {install_dir}")
    print_info(f"Para desinstalar: {uninstaller}")
    
    return True

def install_linux():
    """Instalar en Linux"""
    print_info("Instalando en Linux...")
    
    # Directorio de instalación
    home = Path.home()
    install_dir = home / '.local' / 'share' / 'CalculadoraProfesional'
    install_dir.mkdir(parents=True, exist_ok=True)
    
    # Copiar archivos
    print_info("Copiando archivos...")
    script_dir = Path(__file__).parent
    
    calc_file = script_dir / 'calculadora_completa.py'
    if calc_file.exists():
        shutil.copy(calc_file, install_dir / 'calculadora_completa.py')
    else:
        print_error("No se encontró calculadora_completa.py")
        return False
    
    # Copiar icono si existe
    if (script_dir / 'icono.ico').exists():
        shutil.copy(script_dir / 'icono.ico', install_dir / 'icono.ico')
    
    print_success("Archivos copiados")
    
    # Crear script ejecutable
    print_info("Creando ejecutable...")
    launcher = install_dir / 'calculadora.sh'
    launcher.write_text(f'''#!/bin/bash
cd "{install_dir}"
python3 calculadora_completa.py
''')
    launcher.chmod(0o755)
    
    # Crear entrada en el menú de aplicaciones
    print_info("Creando entrada en el menú...")
    desktop_dir = home / '.local' / 'share' / 'applications'
    desktop_dir.mkdir(parents=True, exist_ok=True)
    
    desktop_file = desktop_dir / 'calculadora-profesional.desktop'
    desktop_file.write_text(f'''[Desktop Entry]
Version=2.0
Type=Application
Name=Calculadora Profesional
Comment=Calculadora científica con soporte para física
Exec={launcher}
Icon={install_dir / 'icono.ico'}
Terminal=false
Categories=Utility;Calculator;Science;Education;
Keywords=calculator;math;science;physics;
StartupNotify=true
''')
    desktop_file.chmod(0o755)
    
    # Actualizar base de datos de aplicaciones
    try:
        subprocess.run(['update-desktop-database', str(desktop_dir)], 
                      stderr=subprocess.DEVNULL)
    except:
        pass
    
    print_success("Entrada en el menú creada")
    
    # Crear desinstalador
    uninstaller = install_dir / 'desinstalar.sh'
    uninstaller.write_text(f'''#!/bin/bash
echo "Desinstalando Calculadora Profesional..."
rm -rf "{install_dir}"
rm -f "{desktop_file}"
rm -f "$HOME/Desktop/calculadora-profesional.desktop"
rm -f "$HOME/Escritorio/calculadora-profesional.desktop"
update-desktop-database "{desktop_dir}" 2>/dev/null
echo "Desinstalación completada"
''')
    uninstaller.chmod(0o755)
    
    print_success(f"Instalación completada en: {install_dir}")
    print_info("Busca 'Calculadora Profesional' en tu menú de aplicaciones")
    print_info(f"Para desinstalar: {uninstaller}")
    
    return True

def main():
    """Función principal"""
    print_header()
    
    # Detectar sistema operativo
    os_type = detect_os()
    print_info(f"Sistema operativo detectado: {os_type.upper()}")
    
    if os_type == "unknown":
        print_error("Sistema operativo no soportado")
        return 1
    
    # Verificar Python
    print_info("Verificando Python...")
    if not check_python_version():
        return 1
    
    # Verificar tkinter
    print_info("Verificando tkinter...")
    if not check_tkinter():
        if os_type == "linux":
            if not install_tkinter_linux():
                return 1
            # Verificar de nuevo
            if not check_tkinter():
                print_error("No se pudo instalar tkinter")
                return 1
        else:
            print_error("tkinter no está disponible")
            print_info("Instala tkinter y vuelve a ejecutar el instalador")
            return 1
    
    print()
    
    # Instalar según el sistema operativo
    try:
        if os_type == "windows":
            success = install_windows()
        elif os_type == "linux":
            success = install_linux()
        elif os_type == "mac":
            print_error("macOS no está soportado aún")
            success = False
        
        if success:
            print()
            print(f"{Colors.GREEN}{Colors.BOLD}{'='*50}")
            print("  ✓ INSTALACIÓN COMPLETADA EXITOSAMENTE")
            print(f"{'='*50}{Colors.END}\n")
            print(f"{Colors.YELLOW}¡Disfruta tu calculadora científica! 🧮{Colors.END}\n")
            return 0
        else:
            print_error("La instalación falló")
            return 1
            
    except Exception as e:
        print_error(f"Error durante la instalación: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Instalación cancelada por el usuario{Colors.END}")
        sys.exit(1)
