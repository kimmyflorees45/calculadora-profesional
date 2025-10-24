# Calculadora Profesional

Calculadora multiplataforma con diseño moderno rosa/morado.

## 🚀 Características

- **Modo Básico**: Operaciones aritméticas estándar
- **Modo Científico**: Funciones trigonométricas, logaritmos, potencias, factorial
- **Juego de Divisiones**: Minijuego educativo integrado
- **Diseño Moderno**: Interfaz rosa/morado con barra superior estilo macOS

## 📱 Plataformas Soportadas

- **Android** (APK)
- **Windows** (EXE)
- **Linux**
- **macOS**

## 🔧 Instalación

### Requisitos
```bash
pip install -r requirements.txt
```

### Ejecutar Localmente
```bash
python calculadora_rosa.py
```

## 📦 Compilar para Android

### Usando Google Colab

1. Abre un nuevo cuaderno en [Google Colab](https://colab.research.google.com/)

2. **Celda 1 - Instalar dependencias:**
```python
!pip install buildozer cython==0.29.33
!sudo apt-get update
!sudo apt-get install -y openjdk-17-jdk zip unzip
```

3. **Celda 2 - Crear proyecto:**
```python
!mkdir -p /content/calculadora
%cd /content/calculadora

# Crear buildozer.spec
spec_content = """[app]
title = CalculadoraPro
package.name = calculadorapro
package.domain = org.calculadora
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
"""

with open('buildozer.spec', 'w') as f:
    f.write(spec_content)

print("✅ Proyecto creado")
```

4. **Celda 3 - Subir calculadora_rosa.py:**
```python
from google.colab import files
print("📤 Sube calculadora_rosa.py")
uploaded = files.upload()
```

5. **Celda 4 - Compilar (30-60 min):**
```python
!buildozer android debug
```

6. **Celda 5 - Descargar APK:**
```python
from google.colab import files
files.download('bin/calculadorapro-1.0-arm64-v8a-debug.apk')
print("✅ APK descargado!")
```

## 📝 Notas

- El archivo principal es `calculadora_rosa.py`
- El archivo `buildozer.spec` es para compilación Android
- Tiempo de compilación: 30-60 minutos (primera vez), 10-15 minutos (con caché)

## 🎨 Colores

- **Rosa pastel**: Fondo general
- **Morado claro**: Barra superior
- **Rosa/Morado**: Botones y elementos UI

## 📄 Licencia

Proyecto personal - Uso libre
