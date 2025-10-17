[app]

# Título de la aplicación
title = Calculadora Profesional

# Nombre del paquete
package.name = calculadoraprofesional

# Dominio del paquete (único en Play Store)
package.domain = com.calculadora

# Directorio del código fuente
source.dir = .

# Archivo principal
source.include_exts = py,png,jpg,kv,atlas,ico

# Versión de la aplicación
version = 2.0

# Requisitos de Python
requirements = python3,kivy

# Icono de la aplicación (si tienes uno)
#icon.filename = %(source.dir)s/icono.png

# Presplash (pantalla de carga)
#presplash.filename = %(source.dir)s/presplash.png

# Orientación (portrait, landscape, o all)
orientation = portrait

# Servicios (ninguno para esta app)
services = 

# Permisos de Android
android.permissions = 

# API mínima de Android (21 = Android 5.0)
android.minapi = 21

# API objetivo de Android
android.api = 31

# NDK API
android.ndk_api = 21

# Arquitecturas a compilar
android.archs = arm64-v8a, armeabi-v7a

# Permitir backup
android.allow_backup = True

[buildozer]

# Directorio de logs
log_level = 2

# Directorio de compilación
# warn_on_root = 1
