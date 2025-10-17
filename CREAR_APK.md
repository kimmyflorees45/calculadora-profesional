# 📱 Crear APK para Android - Calculadora Profesional

## 🎯 Opciones para Crear el APK

### OPCIÓN 1: Usar Servicio Online (MÁS FÁCIL) ⭐ RECOMENDADO

**Kivy Buildozer Online:**
1. Ve a: https://kivy.org/#download
2. O usa Google Colab con este notebook

**Google Colab (GRATIS):**
```python
# Ejecuta esto en Google Colab:
!pip install buildozer
!pip install cython
!buildozer android debug
```

### OPCIÓN 2: Compilar en Linux/WSL

#### Requisitos:
- Ubuntu/Debian (o WSL en Windows)
- Python 3.8+
- Java JDK
- Android SDK

#### Pasos:

**1. Instalar dependencias:**
```bash
sudo apt update
sudo apt install -y python3-pip build-essential git zip unzip \
    openjdk-11-jdk autoconf libtool pkg-config zlib1g-dev \
    libncurses5-dev libncursesw5-dev libtinfo5 cmake \
    libffi-dev libssl-dev
```

**2. Instalar Buildozer:**
```bash
pip3 install buildozer
pip3 install cython
```

**3. Compilar APK:**
```bash
cd android
buildozer android debug
```

**4. El APK estará en:**
```
android/bin/calculadoraprofesional-2.0-debug.apk
```

### OPCIÓN 3: Usar GitHub Actions (AUTOMÁTICO)

Crea `.github/workflows/build-apk.yml`:

```yaml
name: Build APK

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    
    - name: Install dependencies
      run: |
        pip install buildozer cython
        sudo apt update
        sudo apt install -y openjdk-11-jdk
    
    - name: Build APK
      run: |
        cd android
        buildozer android debug
    
    - name: Upload APK
      uses: actions/upload-artifact@v2
      with:
        name: calculadora-apk
        path: android/bin/*.apk
```

## 🚀 Método Rápido con Docker

```bash
docker run --rm -v "$PWD":/app kivy/buildozer android debug
```

## 📦 Archivos Necesarios

```
android/
├── calculadora_android.py  (código principal)
├── buildozer.spec          (configuración)
└── icono.png              (opcional, icono de la app)
```

## 🎨 Personalizar el APK

### Cambiar Icono:
1. Crea un icono PNG de 512x512
2. Guárdalo como `icono.png`
3. Descomenta en `buildozer.spec`:
   ```
   icon.filename = %(source.dir)s/icono.png
   ```

### Cambiar Nombre:
En `buildozer.spec`:
```
title = Tu Nombre
package.name = tunombre
package.domain = com.tudominio
```

## 📱 Instalar el APK en Android

### Método 1: Transferir por USB
1. Conecta tu teléfono
2. Copia el APK al teléfono
3. Abre el archivo APK
4. Permite "Instalar desde fuentes desconocidas"
5. Instala

### Método 2: Subir a Google Drive
1. Sube el APK a Google Drive
2. Descárgalo desde tu teléfono
3. Instala

### Método 3: Usar ADB
```bash
adb install bin/calculadoraprofesional-2.0-debug.apk
```

## 🌐 Publicar en Play Store

1. **Crear cuenta de desarrollador** ($25 único)
2. **Compilar versión release:**
   ```bash
   buildozer android release
   ```
3. **Firmar el APK** con tu keystore
4. **Subir a Play Console**

## ⚠️ Solución de Problemas

### Error: "buildozer: command not found"
```bash
pip3 install --user buildozer
export PATH=$PATH:~/.local/bin
```

### Error: "SDK not found"
Buildozer descargará el SDK automáticamente en la primera compilación.

### Error: "Java not found"
```bash
sudo apt install openjdk-11-jdk
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

### Compilación muy lenta
Primera vez: 30-60 minutos (descarga SDK, NDK, etc.)
Siguientes: 5-10 minutos

## 📊 Tamaño del APK

- **Debug**: ~15-20 MB
- **Release**: ~10-15 MB (optimizado)

## ✨ Características del APK

✅ Funciona offline (no requiere internet)
✅ Compatible con Android 5.0+
✅ Interfaz optimizada para móvil
✅ Botones grandes para touch
✅ Modo científico completo
✅ Números negativos
✅ Operador de potencia ^
✅ Todas las funciones de la versión desktop

## 🎯 Alternativa Rápida: Progressive Web App (PWA)

Si no quieres compilar APK, puedes hacer una PWA:

1. Sube la calculadora a un servidor web
2. Agrega `manifest.json`
3. Los usuarios pueden "Agregar a pantalla de inicio"
4. Funciona como app nativa

## 📝 Notas

- El APK generado es para **pruebas** (debug)
- Para Play Store necesitas versión **release firmada**
- La primera compilación tarda mucho (descarga herramientas)
- Compilaciones siguientes son más rápidas

---

**¿Necesitas ayuda?** 
- Documentación Kivy: https://kivy.org/doc/stable/
- Buildozer: https://buildozer.readthedocs.io/
