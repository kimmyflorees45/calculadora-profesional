# 🧮 Calculadora Profesional - Página Web

Página web promocional con diseño morado pastel para la Calculadora Profesional.

## 🎨 Características del Diseño

- **Colores:** Morado y rosa pastel
- **Fuente:** Poppins (Google Fonts)
- **Animaciones:** Suaves y elegantes
- **Responsive:** Se adapta a todos los dispositivos
- **Legal:** Cookies, Términos y Privacidad incluidos

## 📁 Archivos

- `index.html` - Página principal
- `terminos.html` - Términos y Condiciones
- `privacidad.html` - Política de Privacidad
- `styles.css` - Estilos y diseño
- `script.js` - Animaciones e interactividad
- `cookies.js` - Sistema de cookies
- `screenshots/` - Carpeta para imágenes

## 🚀 Cómo Usar

### Opción 1: Abrir Localmente
1. Abre `index.html` en tu navegador
2. ¡Listo!

### Opción 2: Servidor Local
```bash
# Con Python
python -m http.server 8000

# Con Node.js
npx http-server
```

Luego abre: `http://localhost:8000`

## 🌐 Publicar en Internet

### GitHub Pages (Gratis)
1. Crea un repositorio en GitHub
2. Sube los archivos de la carpeta `website`
3. Ve a Settings → Pages
4. Selecciona la rama `main`
5. ¡Tu sitio estará en: `https://tuusuario.github.io/calculadora`!

### Netlify (Gratis)
1. Arrastra la carpeta `website` a netlify.com/drop
2. ¡Listo! Te dan una URL automáticamente

### Vercel (Gratis)
1. Instala Vercel CLI: `npm i -g vercel`
2. En la carpeta website: `vercel`
3. Sigue las instrucciones

## 📝 Personalizar

### Cambiar Colores
Edita las variables en `styles.css`:
```css
:root {
    --purple-500: #A855F7;
    --pink-500: #EC4899;
    /* Cambia estos valores */
}
```

### Cambiar Textos
Edita `index.html` directamente.

### Agregar Más Secciones
Copia una sección existente y modifícala.

## 🔗 Enlaces de Descarga

Asegúrate de que las rutas en los botones de descarga apunten a tus archivos:

```html
<!-- Windows -->
<a href="../dist/CalculadoraProfesional-Windows.exe" download>

<!-- macOS -->
<a href="../macos/CalculadoraProfesional-macOS.zip" download>

<!-- Linux -->
<a href="../dist/CalculadoraProfesional-Linux.tar.gz" download>

<!-- Android -->
<a href="../android/calculadora.apk" download>
```

## 📸 Capturas de Pantalla

La página incluye mockups animados de:
- Windows
- macOS
- Linux
- Android

Puedes reemplazarlos con capturas reales si lo deseas.

## ✨ Efectos Incluidos

- ✅ Scroll suave
- ✅ Animaciones al hacer scroll
- ✅ Contadores animados
- ✅ Efecto parallax
- ✅ Partículas flotantes
- ✅ Hover effects
- ✅ Notificaciones de descarga
- ✅ Formas flotantes en el fondo

## 🎯 SEO

Para mejorar el SEO, agrega en `<head>`:

```html
<meta name="description" content="Calculadora profesional gratis con modo científico y juego educativo. Disponible para Windows, macOS, Linux y Android.">
<meta name="keywords" content="calculadora, científica, gratis, windows, mac, linux, android">
<meta property="og:title" content="Calculadora Profesional">
<meta property="og:description" content="La calculadora más hermosa y completa">
<meta property="og:image" content="preview.png">
```

## 📱 Responsive

La página se adapta perfectamente a:
- 📱 Móviles (320px+)
- 📱 Tablets (768px+)
- 💻 Laptops (1024px+)
- 🖥️ Desktops (1440px+)

## 🎨 Paleta de Colores

```
Morado Claro: #FAF5FF
Morado Pastel: #E9D5FF
Morado: #A855F7
Morado Oscuro: #7E22CE
Rosa Claro: #FCE7F3
Rosa Pastel: #FBCFE8
Rosa: #EC4899
Rosa Oscuro: #DB2777
```

## 🚀 Optimizaciones

- ✅ CSS minificado (puedes usar cssnano)
- ✅ Lazy loading de imágenes
- ✅ Animaciones optimizadas
- ✅ Sin dependencias pesadas

## 📄 Licencia

Libre para usar y modificar.

---

**¡Disfruta tu hermosa página web! 💜**
