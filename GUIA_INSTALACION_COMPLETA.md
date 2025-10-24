# 🚀 Guía Completa: Subir tu Calculadora a Internet

## Paso 1: Instalar Git

### Descargar Git para Windows
1. Ve a: https://git-scm.com/download/windows
2. Descarga "64-bit Git for Windows Setup"
3. Ejecuta el instalador
4. **Importante**: En la instalación, selecciona:
   - ✅ "Git from the command line and also from 3rd-party software"
   - ✅ "Use Windows' default console window"
5. Haz clic en "Next" hasta finalizar
6. **Reinicia tu terminal/IDE** después de instalar

### Verificar instalación
Abre una nueva terminal y ejecuta:
```bash
git --version
```
Deberías ver algo como: `git version 2.43.0`

## Paso 2: Crear Cuenta en GitHub

1. Ve a: https://github.com/signup
2. Ingresa tu email
3. Crea una contraseña
4. Elige un nombre de usuario (ejemplo: `kimyb-dev`)
5. Verifica tu email
6. ¡Listo!

## Paso 3: Crear el Repositorio en GitHub

1. Inicia sesión en GitHub
2. Haz clic en el botón "+" (arriba derecha) → "New repository"
3. Configuración:
   - **Repository name**: `calculadora-profesional`
   - **Description**: `Calculadora científica con modo básico, científico y juego de divisiones educativo`
   - **Public** (seleccionado)
   - ❌ NO marques "Add a README file"
   - ❌ NO agregues .gitignore (ya lo tenemos)
   - ❌ NO agregues licencia por ahora
4. Haz clic en "Create repository"

**Guarda la URL que aparece**, será algo como:
```
https://github.com/TU_USUARIO/calculadora-profesional.git
```

## Paso 4: Subir el Código a GitHub

Abre una terminal en la carpeta de tu proyecto y ejecuta estos comandos **UNO POR UNO**:

```bash
# 1. Navegar a tu proyecto
cd "c:\Users\kimyb\OneDrive\Calculadora python"

# 2. Inicializar Git
git init

# 3. Configurar tu identidad (reemplaza con tus datos)
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"

# 4. Agregar todos los archivos (excepto los de .gitignore)
git add .

# 5. Ver qué archivos se van a subir
git status

# 6. Hacer el primer commit
git commit -m "Primera versión de la calculadora profesional"

# 7. Conectar con GitHub (reemplaza TU_USUARIO con tu usuario de GitHub)
git remote add origin https://github.com/TU_USUARIO/calculadora-profesional.git

# 8. Cambiar a la rama main
git branch -M main

# 9. Subir el código
git push -u origin main
```

**Nota**: Te pedirá tu usuario y contraseña de GitHub.

## Paso 5: Crear el Release con los Ejecutables

### 5.1 Preparar los Archivos

Primero, necesitamos organizar los ejecutables:

**Windows:**
- Archivo: `CalculadoraProfesional.exe` (ya existe en la raíz)
- Tamaño: ~10 MB

**Linux:**
- Archivo: `dist/CalculadoraProfesional-Linux.tar.gz` (ya existe)
- Tamaño: ~33 KB

**macOS:**
- Necesitamos crear un ZIP para macOS

### 5.2 Crear el Release en GitHub

1. Ve a tu repositorio en GitHub: `https://github.com/TU_USUARIO/calculadora-profesional`
2. Haz clic en "Releases" (lado derecho, debajo de "About")
3. Haz clic en "Create a new release"
4. Configuración del Release:

   **Tag version**: `v1.0.0`
   
   **Release title**: `Calculadora Profesional v1.0.0 - Primera Versión 🎉`
   
   **Description**:
   ```markdown
   ## 🎉 Primera Versión Oficial
   
   Calculadora científica profesional con interfaz hermosa en rosa y morado.
   
   ### ✨ Características
   
   - 🔢 **Modo Básico**: Operaciones aritméticas simples
   - 🔬 **Modo Científico**: Funciones trigonométricas, logaritmos, potencias
   - 🎮 **Juego de Divisiones**: Aprende matemáticas jugando
   - 🎨 **Diseño Hermoso**: Colores rosa y morado pastel
   - ⚡ **Súper Rápida**: Sin publicidad ni retrasos
   - 🌍 **Multi-Plataforma**: Windows, macOS y Linux
   
   ### 📥 Instrucciones de Descarga
   
   #### Windows
   1. Descarga `CalculadoraProfesional.exe`
   2. Doble clic para ejecutar
   3. ¡Listo!
   
   #### Linux
   1. Descarga `CalculadoraProfesional-Linux.tar.gz`
   2. Extrae el archivo
   3. Ejecuta el instalador
   
   #### macOS
   1. Descarga `CalculadoraProfesional-macOS.zip`
   2. Extrae el archivo
   3. Ejecuta el instalador
   
   ### 📊 Requisitos del Sistema
   
   - **Windows**: Windows 10 o superior
   - **Linux**: Cualquier distribución moderna
   - **macOS**: macOS 10.13 o superior
   
   ---
   
   **100% Gratis • Sin Publicidad • Código Abierto**
   ```

5. **Arrastra los archivos** a la sección "Attach binaries by dropping them here":
   - `CalculadoraProfesional.exe`
   - `CalculadoraProfesional-Linux.tar.gz`
   - (Si tienes el ZIP de macOS, súbelo también)

6. Haz clic en "Publish release"

### 5.3 Copiar las URLs de Descarga

Después de publicar, verás URLs como:
```
https://github.com/TU_USUARIO/calculadora-profesional/releases/download/v1.0.0/CalculadoraProfesional.exe
https://github.com/TU_USUARIO/calculadora-profesional/releases/download/v1.0.0/CalculadoraProfesional-Linux.tar.gz
```

**¡Guarda estas URLs!** Las necesitaremos para el siguiente paso.

## Paso 6: Actualizar el HTML con las URLs de GitHub

Ahora voy a actualizar automáticamente el archivo `index.html` para que use las URLs de GitHub Releases.

**Espera a que te dé las URLs exactas después de crear el release.**

## Paso 7: Crear Cuenta en Netlify

1. Ve a: https://app.netlify.com/signup
2. Haz clic en "Sign up with GitHub"
3. Autoriza Netlify para acceder a tu GitHub
4. ¡Listo!

## Paso 8: Desplegar en Netlify

### Opción A: Conectar GitHub (Recomendado - Automático)

1. En Netlify, haz clic en "Add new site" → "Import an existing project"
2. Selecciona "Deploy with GitHub"
3. Busca y selecciona `calculadora-profesional`
4. Configuración:
   - **Branch to deploy**: `main`
   - **Base directory**: `website`
   - **Build command**: (dejar vacío)
   - **Publish directory**: `website`
5. Haz clic en "Deploy site"
6. Espera 1-2 minutos

### Opción B: Arrastrar y Soltar (Manual)

1. En Netlify, ve al área de "Sites"
2. Arrastra la carpeta `website` completa
3. Espera a que se despliegue

## Paso 9: Configurar Dominio en Netlify

1. Una vez desplegado, Netlify te dará una URL como:
   ```
   https://random-name-123456.netlify.app
   ```

2. Para cambiar el nombre:
   - Ve a "Site settings" → "Site details"
   - Haz clic en "Change site name"
   - Ingresa: `calculadora-profesional` (o el que prefieras)
   - Tu URL será: `https://calculadora-profesional.netlify.app`

## Paso 10: Verificar que Todo Funciona

1. **Página web**: Abre `https://tu-sitio.netlify.app`
2. **Descargas**: Haz clic en cada botón de descarga
3. **Ejecutables**: Verifica que se descarguen desde GitHub

## 🎉 ¡Listo!

Tu calculadora ya está en internet:
- **Código**: `https://github.com/TU_USUARIO/calculadora-profesional`
- **Descargas**: `https://github.com/TU_USUARIO/calculadora-profesional/releases`
- **Página Web**: `https://tu-sitio.netlify.app`

## 🔄 Para Actualizar en el Futuro

### Actualizar el Código:
```bash
git add .
git commit -m "Descripción de los cambios"
git push
```
Netlify desplegará automáticamente en 1-2 minutos.

### Actualizar los Ejecutables:
1. Ve a GitHub → Releases → "Draft a new release"
2. Tag: `v1.1.0` (incrementa la versión)
3. Sube los nuevos archivos
4. Publica el release

## 📞 Ayuda

Si algo no funciona:
1. Verifica que Git esté instalado: `git --version`
2. Verifica que estés en la carpeta correcta
3. Lee los mensajes de error cuidadosamente
4. Avísame y te ayudo

---

**¡Vamos a hacerlo paso a paso! 🚀**
