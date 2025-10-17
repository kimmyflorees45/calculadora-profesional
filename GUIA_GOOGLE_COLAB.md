# 📱 Crear APK en Google Colab - Guía Paso a Paso

## 🎯 ¿Qué es Google Colab?

Google Colab es un servicio **GRATIS** de Google que te da una computadora virtual en la nube con Linux. Perfecto para compilar APKs sin instalar nada en tu PC.

---

## 📋 PASO 1: Preparar los Archivos

### 1.1 Sube tus archivos a Google Drive

1. **Abre Google Drive**: https://drive.google.com
2. **Crea una carpeta** llamada `CalculadoraAPK`
3. **Sube estos archivos** a esa carpeta:
   - `calculadora_android.py`
   - `buildozer.spec`
   - `icono.ico` (opcional)

**Captura de pantalla de cómo debe verse:**
```
Google Drive/
└── CalculadoraAPK/
    ├── calculadora_android.py
    ├── buildozer.spec
    └── icono.ico
```

---

## 📋 PASO 2: Abrir Google Colab

1. **Ve a**: https://colab.research.google.com
2. **Haz clic en**: "Nuevo cuaderno" o "New notebook"
3. **Verás una pantalla** con celdas de código

**Consejo:** Guarda el cuaderno como "Compilar_APK_Calculadora"

---

## 📋 PASO 3: Conectar Google Drive

### 3.1 En la primera celda, copia y pega:

```python
# Montar Google Drive
from google.colab import drive
drive.mount('/content/drive')
```

### 3.2 Ejecuta la celda:
- Haz clic en el **botón de Play ▶** a la izquierda
- O presiona **Shift + Enter**

### 3.3 Autoriza el acceso:
1. Te aparecerá un enlace
2. Haz clic en el enlace
3. Selecciona tu cuenta de Google
4. Copia el código que te da
5. Pégalo en Colab
6. Presiona Enter

**Verás:** "Mounted at /content/drive" ✅

---

## 📋 PASO 4: Navegar a tu Carpeta

### 4.1 En una nueva celda, copia:

```python
# Ir a la carpeta de tu proyecto
%cd /content/drive/MyDrive/CalculadoraAPK
!ls -la
```

### 4.2 Ejecuta (Shift + Enter)

**Verás:** La lista de tus archivos
```
calculadora_android.py
buildozer.spec
icono.ico
```

---

## 📋 PASO 5: Instalar Dependencias

### 5.1 En una nueva celda, copia TODO esto:

```bash
# Instalar dependencias necesarias
!apt-get update
!apt-get install -y python3-pip build-essential git zip unzip \
    openjdk-11-jdk autoconf libtool pkg-config zlib1g-dev \
    libncurses5-dev libncursesw5-dev libtinfo5 cmake \
    libffi-dev libssl-dev

# Instalar Buildozer y Cython
!pip install buildozer
!pip install cython==0.29.33
!pip install kivy

# Verificar instalación
!buildozer --version
```

### 5.2 Ejecuta (Shift + Enter)

**Esto tardará:** 3-5 minutos ⏱️

**Verás:** Muchas líneas de instalación

**Al final verás:** "Buildozer 1.x.x" ✅

---

## 📋 PASO 6: Compilar el APK (¡El momento importante!)

### 6.1 En una nueva celda, copia:

```bash
# Compilar APK
!buildozer android debug
```

### 6.2 Ejecuta (Shift + Enter)

**⚠️ IMPORTANTE:**
- **Primera vez:** Tardará 30-60 minutos (descarga Android SDK, NDK, etc.)
- **Siguientes veces:** Solo 5-10 minutos
- **No cierres la pestaña** mientras compila

**Verás:**
```
# Downloading Android SDK...
# Downloading Android NDK...
# Compiling...
# Building APK...
```

**Al final verás:**
```
# APK generated successfully!
# APK: /content/drive/MyDrive/CalculadoraAPK/bin/calculadoraprofesional-2.0-debug.apk
```

✅ **¡Éxito!**

---

## 📋 PASO 7: Encontrar tu APK

### 7.1 El APK está en:

```
Google Drive/
└── CalculadoraAPK/
    └── bin/
        └── calculadoraprofesional-2.0-debug.apk
```

### 7.2 Para verificar, ejecuta:

```bash
# Ver el APK generado
!ls -lh bin/*.apk
```

**Verás:**
```
-rw-r--r-- 1 root root 15M calculadoraprofesional-2.0-debug.apk
```

---

## 📋 PASO 8: Descargar el APK

### Opción A - Desde Google Drive:
1. Abre Google Drive en tu navegador
2. Ve a `CalculadoraAPK/bin/`
3. Haz clic derecho en el APK
4. **Descargar**

### Opción B - Desde Colab:
```python
# Descargar directamente desde Colab
from google.colab import files
files.download('/content/drive/MyDrive/CalculadoraAPK/bin/calculadoraprofesional-2.0-debug.apk')
```

---

## 📋 PASO 9: Instalar en tu Android

### 9.1 Transferir el APK a tu teléfono:

**Método 1 - USB:**
1. Conecta tu teléfono a la PC
2. Copia el APK al teléfono

**Método 2 - Google Drive:**
1. Abre Google Drive en tu teléfono
2. Descarga el APK

**Método 3 - Email/WhatsApp:**
1. Envíate el APK por email o WhatsApp
2. Descárgalo en tu teléfono

### 9.2 Instalar:
1. Abre el archivo APK en tu teléfono
2. Si te pide, **permite "Instalar desde fuentes desconocidas"**
3. Toca **Instalar**
4. ¡Listo! 🎉

---

## 🎓 NOTEBOOK COMPLETO (Copia todo de una vez)

```python
# ========================================
# COMPILAR APK - CALCULADORA PROFESIONAL
# ========================================

# PASO 1: Montar Google Drive
from google.colab import drive
drive.mount('/content/drive')

# PASO 2: Ir a la carpeta del proyecto
%cd /content/drive/MyDrive/CalculadoraAPK
!ls -la

# PASO 3: Instalar dependencias
!apt-get update -qq
!apt-get install -y python3-pip build-essential git zip unzip \
    openjdk-11-jdk autoconf libtool pkg-config zlib1g-dev \
    libncurses5-dev libncursesw5-dev libtinfo5 cmake \
    libffi-dev libssl-dev > /dev/null 2>&1

!pip install -q buildozer cython==0.29.33 kivy

# PASO 4: Verificar instalación
!buildozer --version

# PASO 5: Compilar APK
print("🚀 Iniciando compilación...")
print("⏱️ Esto puede tardar 30-60 minutos la primera vez")
!buildozer android debug

# PASO 6: Verificar APK generado
print("\n✅ APK generado:")
!ls -lh bin/*.apk

# PASO 7: Descargar APK
from google.colab import files
files.download('/content/drive/MyDrive/CalculadoraAPK/bin/calculadoraprofesional-2.0-debug.apk')

print("\n🎉 ¡Compilación completada!")
```

---

## 🔧 Solución de Problemas

### ❌ Error: "buildozer: command not found"
**Solución:**
```bash
!pip install --upgrade buildozer
```

### ❌ Error: "Java not found"
**Solución:**
```bash
!apt-get install -y openjdk-11-jdk
```

### ❌ Error: "Permission denied"
**Solución:**
```bash
!chmod +x buildozer.spec
!chmod +x calculadora_android.py
```

### ❌ La compilación se detiene
**Solución:**
- Colab tiene límite de tiempo (12 horas)
- Si se detiene, ejecuta de nuevo desde el PASO 6
- Los archivos descargados se guardan, no empieza desde cero

### ❌ APK muy grande (>50 MB)
**Normal:** La primera vez incluye todas las librerías
**Solución:** Usa `buildozer android release` para optimizar

---

## 💡 Consejos

### ✅ Guardar progreso:
- Colab guarda todo en Google Drive
- Puedes cerrar y volver después
- Los archivos descargados permanecen

### ✅ Compilar más rápido:
- Segunda vez: Solo 5-10 minutos
- Buildozer reutiliza archivos descargados

### ✅ Versión Release (para Play Store):
```bash
!buildozer android release
```

### ✅ Limpiar caché (si hay errores):
```bash
!buildozer android clean
!buildozer android debug
```

---

## 📊 Tiempos Estimados

| Paso | Tiempo |
|------|--------|
| Montar Drive | 10 segundos |
| Instalar dependencias | 3-5 minutos |
| Primera compilación | 30-60 minutos |
| Compilaciones siguientes | 5-10 minutos |
| Descargar APK | 1-2 minutos |

**Total primera vez:** ~40-70 minutos
**Total siguientes:** ~10-15 minutos

---

## 🎯 Checklist

Antes de compilar, verifica:
- [ ] Archivos subidos a Google Drive
- [ ] Google Colab abierto
- [ ] Drive montado correctamente
- [ ] En la carpeta correcta
- [ ] Dependencias instaladas

Durante la compilación:
- [ ] No cerrar la pestaña
- [ ] Tener buena conexión a internet
- [ ] Esperar pacientemente

Después de compilar:
- [ ] APK generado en `bin/`
- [ ] APK descargado
- [ ] Transferido al teléfono
- [ ] Instalado correctamente

---

## 🆘 ¿Necesitas Ayuda?

### Si algo no funciona:
1. Lee el mensaje de error completo
2. Busca en la sección "Solución de Problemas"
3. Intenta limpiar y recompilar
4. Verifica que los archivos estén correctos

### Recursos útiles:
- Documentación Buildozer: https://buildozer.readthedocs.io/
- Foro Kivy: https://kivy.org/doc/stable/
- Stack Overflow: Busca "buildozer android"

---

## 🎉 ¡Éxito!

Una vez que tengas tu APK:
- Instálalo en tu teléfono
- Prueba todas las funciones
- Compártelo con amigos
- (Opcional) Súbelo a Play Store

**¡Felicidades! Has creado tu primera app Android con Python** 🎊

---

**Versión:** 1.0  
**Última actualización:** 2025  
**Plataforma:** Google Colab (Gratis)
