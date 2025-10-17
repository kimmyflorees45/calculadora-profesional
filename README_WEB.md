# 🌐 Instalación Web - Calculadora Profesional

Este directorio contiene los archivos necesarios para crear una página web de descarga e instalación automática, similar a como funcionan aplicaciones como Discord, VS Code, etc.

## 📁 Archivos Incluidos

```
web/
├── index.html              # Página web principal
├── instalar_web.sh         # Script de instalación automática para Linux
├── README_WEB.md          # Este archivo
└── [archivos a copiar]
    ├── calculadora_completa.py
    ├── CalculadoraProfesional.exe
    ├── instalar.bat
    ├── icono.ico
    └── CalculadoraProfesional_Linux.zip
```

## 🚀 Cómo Funciona

### Para el Usuario:

1. **Entra a la página web** (ej: `tudominio.com/calculadora`)
2. **La página detecta automáticamente** su sistema operativo (Windows/Linux)
3. **Hace clic en "Descargar"**
4. **Ejecuta el instalador** descargado
5. **¡Listo!** La aplicación está instalada

### Detección Automática:

- **Windows**: Descarga el `.exe` o el `instalar.bat`
- **Linux**: Descarga el script `instalar_web.sh` que instala todo automáticamente
- **Otro SO**: Muestra opciones manuales

## 📤 Cómo Hospedar la Página Web

### Opción 1: GitHub Pages (GRATIS) ⭐ Recomendado

1. **Crea un repositorio en GitHub**
2. **Sube los archivos** de la carpeta `web/` al repositorio
3. **Activa GitHub Pages:**
   - Ve a Settings → Pages
   - Selecciona la rama `main` y carpeta `/root`
   - Guarda
4. **Tu página estará en:** `https://tu-usuario.github.io/nombre-repo/`

**Ejemplo de estructura:**
```
tu-repo/
├── index.html
├── instalar_web.sh
├── calculadora_completa.py
├── CalculadoraProfesional.exe
├── instalar.bat
├── icono.ico
└── CalculadoraProfesional_Linux.zip
```

### Opción 2: Netlify (GRATIS)

1. **Crea cuenta en [Netlify](https://www.netlify.com/)**
2. **Arrastra la carpeta `web/`** a Netlify Drop
3. **¡Listo!** Tu sitio está en línea

### Opción 3: Vercel (GRATIS)

1. **Crea cuenta en [Vercel](https://vercel.com/)**
2. **Importa desde GitHub** o sube los archivos
3. **Deploy automático**

### Opción 4: Tu Propio Servidor

Si tienes un servidor web (Apache, Nginx, etc.):

```bash
# Copiar archivos al directorio web
sudo cp -r web/* /var/www/html/calculadora/

# Dar permisos
sudo chmod 644 /var/www/html/calculadora/*
sudo chmod 755 /var/www/html/calculadora/*.sh
```

## 🔗 Instalación con Un Solo Comando (Linux)

Una vez hospedado, los usuarios de Linux pueden instalar con:

```bash
curl -sSL https://tu-dominio.com/instalar_web.sh | bash
```

O:

```bash
wget -qO- https://tu-dominio.com/instalar_web.sh | bash
```

## 📋 Preparar Archivos para Subir

1. **Copia estos archivos a la carpeta `web/`:**

```bash
# Desde el directorio dist/
cp calculadora_completa.py web/
cp CalculadoraProfesional.exe web/
cp instalar.bat web/
cp icono.ico web/
cp CalculadoraProfesional_Linux.zip web/
cp instalar_linux.sh web/instalador_linux.sh
```

2. **Verifica que todos los archivos estén:**

```
web/
├── index.html                          ✓
├── instalar_web.sh                     ✓
├── calculadora_completa.py             ✓
├── CalculadoraProfesional.exe          ✓
├── instalar.bat                        ✓
├── instalador_linux.sh                 ✓
├── icono.ico                           ✓
└── CalculadoraProfesional_Linux.zip    ✓
```

## 🎨 Personalizar la Página

Edita `index.html` para:

- Cambiar colores (busca los gradientes CSS)
- Modificar el título y descripción
- Agregar más características
- Cambiar el logo (emoji 🧮)
- Agregar capturas de pantalla

## 🔒 Seguridad

### Para GitHub Pages:

Los archivos son públicos, pero eso está bien para software gratuito. Si quieres protección:

1. **Usa GitHub Releases** para archivos grandes
2. **Modifica `index.html`** para descargar desde Releases:

```javascript
const GITHUB_REPO = 'tu-usuario/tu-repo';
const VERSION = 'v2.0';
const downloadUrl = `https://github.com/${GITHUB_REPO}/releases/download/${VERSION}/CalculadoraProfesional.exe`;
```

## 📊 Estadísticas de Descarga

### Con GitHub:

- Ve a "Insights" → "Traffic" para ver visitas
- En "Releases" puedes ver cuántas descargas

### Con Google Analytics:

Agrega antes de `</head>` en `index.html`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=TU-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'TU-ID');
</script>
```

## 🌍 Ejemplo de URLs

Una vez hospedado, tus usuarios podrán:

### Visitar la página:
```
https://tu-usuario.github.io/calculadora-profesional/
```

### Instalar directamente (Linux):
```bash
curl -sSL https://tu-usuario.github.io/calculadora-profesional/instalar_web.sh | bash
```

### Descargar archivos individuales:
```
https://tu-usuario.github.io/calculadora-profesional/CalculadoraProfesional.exe
https://tu-usuario.github.io/calculadora-profesional/instalar.bat
```

## ✅ Checklist de Publicación

- [ ] Copiar todos los archivos a la carpeta `web/`
- [ ] Probar `index.html` localmente (abrir en navegador)
- [ ] Crear repositorio en GitHub
- [ ] Subir archivos
- [ ] Activar GitHub Pages
- [ ] Probar la URL pública
- [ ] Probar descarga en Windows
- [ ] Probar descarga e instalación en Linux
- [ ] Compartir el enlace

## 🎯 Resultado Final

Los usuarios verán una página profesional que:

✅ Detecta automáticamente su sistema operativo  
✅ Muestra el botón de descarga correcto  
✅ Incluye instrucciones claras  
✅ Permite instalación con un clic  
✅ Se ve bien en móvil y escritorio  

## 📱 Compartir

Una vez publicado, comparte el enlace:

- En redes sociales
- En foros de matemáticas/física
- Con tus compañeros de clase
- En comunidades de programación

---

**¿Necesitas ayuda?** Revisa la documentación de:
- [GitHub Pages](https://pages.github.com/)
- [Netlify](https://docs.netlify.com/)
- [Vercel](https://vercel.com/docs)
