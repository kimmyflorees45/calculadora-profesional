# 📦 Cómo Subir tus Aplicaciones a la Página Web

## ❌ Problema
Los archivos ejecutables (.exe, .zip, .tar.gz) son muy pesados para Git/Netlify.

## ✅ Solución: GitHub Releases

### Paso 1: Crear un Repositorio en GitHub

1. Ve a https://github.com
2. Haz clic en "New repository"
3. Nombre: `calculadora-profesional`
4. Descripción: "Calculadora científica con modo básico, científico y juego de divisiones"
5. Público
6. Haz clic en "Create repository"

### Paso 2: Subir el Código (sin ejecutables)

```bash
cd "c:\Users\kimyb\OneDrive\Calculadora python"

# Inicializar Git
git init

# Agregar archivos (el .gitignore ya excluye dist/)
git add .

# Hacer commit
git commit -m "Primera versión de la calculadora"

# Conectar con GitHub (reemplaza TU_USUARIO)
git remote add origin https://github.com/TU_USUARIO/calculadora-profesional.git

# Subir
git branch -M main
git push -u origin main
```

### Paso 3: Crear un Release con los Ejecutables

1. Ve a tu repositorio en GitHub
2. Haz clic en "Releases" (lado derecho)
3. Haz clic en "Create a new release"
4. Tag version: `v1.0.0`
5. Release title: `Calculadora Profesional v1.0.0`
6. Descripción:
   ```
   ## 🎉 Primera versión oficial
   
   ### ✨ Características
   - Calculadora básica
   - Calculadora científica
   - Juego de divisiones educativo
   - Interfaz rosa/morado hermosa
   
   ### 📥 Descargas
   Elige tu sistema operativo:
   - **Windows**: Descarga el archivo .exe
   - **macOS**: Descarga el archivo .zip
   - **Linux**: Descarga el archivo .tar.gz
   ```

7. **Arrastra los archivos ejecutables** a la sección "Attach binaries":
   - `CalculadoraProfesional.exe` (desde la raíz)
   - `dist/CalculadoraProfesional-Linux.tar.gz`
   - Crea un ZIP para macOS si no existe

8. Haz clic en "Publish release"

### Paso 4: Actualizar los Enlaces en el HTML

Después de crear el release, GitHub te dará URLs como:
```
https://github.com/TU_USUARIO/calculadora-profesional/releases/download/v1.0.0/CalculadoraProfesional.exe
```

Actualiza el `index.html` con estas URLs:

```html
<!-- Windows -->
<a href="https://github.com/TU_USUARIO/calculadora-profesional/releases/download/v1.0.0/CalculadoraProfesional.exe" 
   class="btn btn-download">
    <span>⬇️ Descargar .EXE</span>
</a>

<!-- Linux -->
<a href="https://github.com/TU_USUARIO/calculadora-profesional/releases/download/v1.0.0/CalculadoraProfesional-Linux.tar.gz" 
   class="btn btn-download">
    <span>⬇️ Descargar .TAR.GZ</span>
</a>

<!-- macOS -->
<a href="https://github.com/TU_USUARIO/calculadora-profesional/releases/download/v1.0.0/CalculadoraProfesional-macOS.zip" 
   class="btn btn-download">
    <span>⬇️ Descargar .ZIP</span>
</a>
```

### Paso 5: Subir la Página Web a Netlify

#### Opción A: Conectar GitHub con Netlify (Recomendado)

1. Ve a https://app.netlify.com
2. Haz clic en "Add new site" → "Import an existing project"
3. Selecciona "GitHub"
4. Autoriza Netlify
5. Selecciona tu repositorio `calculadora-profesional`
6. Configuración:
   - **Base directory**: `website`
   - **Build command**: (dejar vacío)
   - **Publish directory**: `website`
7. Haz clic en "Deploy site"

#### Opción B: Arrastrar y Soltar

1. Ve a https://app.netlify.com
2. Arrastra la carpeta `website` al área de "Drop"
3. Espera a que se despliegue

### Paso 6: Configurar Dominio Personalizado (Opcional)

1. En Netlify, ve a "Site settings" → "Domain management"
2. Haz clic en "Add custom domain"
3. Ingresa tu dominio (ej: `calculadora-profesional.com`)
4. Sigue las instrucciones para configurar DNS

## 🔄 Para Actualizar en el Futuro

### Actualizar el Código:
```bash
git add .
git commit -m "Descripción de cambios"
git push
```
Netlify desplegará automáticamente.

### Actualizar los Ejecutables:
1. Ve a GitHub → Releases
2. Haz clic en "Draft a new release"
3. Tag: `v1.1.0` (incrementa la versión)
4. Sube los nuevos ejecutables
5. Actualiza las URLs en `index.html` si cambia la versión

## 📊 Ventajas de este Método

✅ **Gratis**: GitHub y Netlify son gratuitos
✅ **Rápido**: CDN global de Netlify
✅ **Profesional**: URLs limpias y releases organizados
✅ **Escalable**: Soporta millones de descargas
✅ **Automático**: Netlify despliega automáticamente al hacer push
✅ **Sin límites**: GitHub Releases soporta archivos de hasta 2GB

## 🎯 Resultado Final

Tu página estará en:
- **Netlify**: `https://tu-sitio.netlify.app`
- **Dominio personalizado**: `https://tu-dominio.com` (opcional)

Las descargas estarán en:
- **GitHub Releases**: `https://github.com/TU_USUARIO/calculadora-profesional/releases`

## 💡 Alternativa: Netlify Large Media

Si prefieres tener todo en Netlify (no recomendado para ejecutables):
```bash
netlify plugins:install netlify-lm-plugin
netlify lm:install
netlify lm:setup
```

Pero GitHub Releases es **mucho mejor** para archivos ejecutables.

---

**¿Necesitas ayuda?** Avísame y te ayudo a configurar todo paso a paso.
