#!/usr/bin/env python3
"""
Script para preparar los archivos para publicación
Crea una carpeta limpia con solo los archivos necesarios
"""

import os
import shutil
from pathlib import Path

def preparar_publicacion():
    print("=" * 60)
    print("  PREPARANDO ARCHIVOS PARA PUBLICACIÓN")
    print("=" * 60)
    print()
    
    # Carpeta de salida
    output_dir = Path("publicar")
    
    # Limpiar carpeta si existe
    if output_dir.exists():
        shutil.rmtree(output_dir)
    
    output_dir.mkdir()
    
    # Archivos a copiar
    archivos_principales = [
        "index.html",
        "terminos.html",
        "privacidad.html",
        "styles.css",
        "script.js",
        "cookies.js"
    ]
    
    print("[*] Copiando archivos principales...")
    for archivo in archivos_principales:
        if Path(archivo).exists():
            shutil.copy2(archivo, output_dir / archivo)
            print(f"  [OK] {archivo}")
        else:
            print(f"  [X] {archivo} (no encontrado)")
    
    # Copiar carpeta screenshots
    print("\n[*] Copiando imagenes...")
    screenshots_src = Path("screenshots")
    screenshots_dst = output_dir / "screenshots"
    
    if screenshots_src.exists():
        screenshots_dst.mkdir()
        
        # Solo copiar archivos SVG
        for archivo in screenshots_src.glob("*.svg"):
            shutil.copy2(archivo, screenshots_dst / archivo.name)
            print(f"  [OK] screenshots/{archivo.name}")
    
    print("\n" + "=" * 60)
    print("  ¡ARCHIVOS LISTOS PARA PUBLICAR!")
    print("=" * 60)
    print()
    print(f"Carpeta creada: {output_dir.absolute()}")
    print()
    print("Archivos incluidos:")
    print("  - 3 paginas HTML")
    print("  - 3 archivos JavaScript/CSS")
    print("  - 3 imagenes SVG")
    print()
    print("SIGUIENTE PASO:")
    print()
    print("OPCIÓN 1 - NETLIFY (Más fácil):")
    print("  1. Ve a: https://app.netlify.com/drop")
    print("  2. Arrastra la carpeta 'publicar' completa")
    print("  3. ¡Listo!")
    print()
    print("OPCIÓN 2 - GITHUB PAGES:")
    print("  1. Crea un repositorio en GitHub")
    print("  2. Sube todos los archivos de la carpeta 'publicar'")
    print("  3. Activa GitHub Pages en Settings")
    print()
    print("OPCIÓN 3 - VERCEL:")
    print("  1. Ve a: https://vercel.com/new")
    print("  2. Arrastra la carpeta 'publicar'")
    print("  3. ¡Listo!")
    print()
    print("Lee COMO_PUBLICAR.txt para más detalles")
    print()

if __name__ == "__main__":
    try:
        preparar_publicacion()
    except Exception as e:
        print(f"\n[ERROR] {e}")
        print("\nAsegurate de ejecutar este script desde la carpeta 'website'")
