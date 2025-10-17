"""
Script para convertir SVG a ICO usando PIL/Pillow
"""
try:
    from PIL import Image
    import cairosvg
    import io
    
    # Convertir SVG a PNG en memoria
    png_data = cairosvg.svg2png(url='icono.svg', output_width=256, output_height=256)
    
    # Abrir con PIL
    img = Image.open(io.BytesIO(png_data))
    
    # Crear diferentes tamaños para el ICO
    img.save('icono.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    
    print("✅ Icono creado exitosamente: icono.ico")
    
except ImportError as e:
    print("⚠️ Faltan dependencias. Instalando...")
    print("Ejecuta: pip install pillow cairosvg")
    
    # Método alternativo sin cairosvg
    try:
        from PIL import Image, ImageDraw, ImageFont
        
        # Crear un icono simple con PIL
        sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
        images = []
        
        for size in sizes:
            img = Image.new('RGBA', size, (245, 230, 240, 255))
            draw = ImageDraw.Draw(img)
            
            # Dibujar un rectángulo redondeado (calculadora)
            margin = size[0] // 8
            rect_coords = [margin, margin, size[0] - margin, size[1] - margin]
            draw.rounded_rectangle(rect_coords, radius=size[0]//10, fill=(255, 255, 255, 255))
            
            # Dibujar display
            display_margin = margin + size[0] // 20
            display_height = size[1] // 6
            draw.rounded_rectangle(
                [display_margin, display_margin, size[0] - display_margin, display_margin + display_height],
                radius=size[0]//30,
                fill=(230, 208, 230, 255)
            )
            
            # Dibujar algunos botones
            button_size = size[0] // 8
            button_margin = display_margin
            button_y = display_margin + display_height + size[0] // 20
            
            for i in range(3):
                for j in range(3):
                    x = button_margin + j * (button_size + size[0] // 40)
                    y = button_y + i * (button_size + size[0] // 40)
                    draw.rounded_rectangle(
                        [x, y, x + button_size, y + button_size],
                        radius=size[0]//40,
                        fill=(230, 208, 230, 255)
                    )
            
            images.append(img)
        
        # Guardar como ICO
        images[0].save('icono.ico', format='ICO', sizes=[(img.width, img.height) for img in images])
        print("✅ Icono simple creado exitosamente: icono.ico")
        
    except Exception as e2:
        print(f"❌ Error: {e2}")
        print("\nMétodo alternativo: Usa un convertidor online:")
        print("1. Ve a: https://convertio.co/es/svg-ico/")
        print("2. Sube el archivo icono.svg")
        print("3. Descarga el icono.ico")

except Exception as e:
    print(f"❌ Error: {e}")
