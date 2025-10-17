# -*- coding: utf-8 -*-
"""Script para crear icono de la calculadora"""
from PIL import Image, ImageDraw

def crear_icono():
    # Crear imagen base de 256x256
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Fondo con gradiente (simulado con rectángulo)
    draw.rounded_rectangle([0, 0, size, size], radius=60, fill=(230, 208, 230, 255))
    
    # Calculadora
    calc_x = 38
    calc_y = 28
    calc_w = 180
    calc_h = 200
    
    # Sombra
    shadow_offset = 4
    draw.rounded_rectangle(
        [calc_x + shadow_offset, calc_y + shadow_offset, 
         calc_x + calc_w + shadow_offset, calc_y + calc_h + shadow_offset],
        radius=20,
        fill=(0, 0, 0, 30)
    )
    
    # Cuerpo de la calculadora
    draw.rounded_rectangle(
        [calc_x, calc_y, calc_x + calc_w, calc_y + calc_h],
        radius=20,
        fill=(255, 255, 255, 242)
    )
    
    # Display
    display_x = calc_x + 15
    display_y = calc_y + 15
    display_w = 150
    display_h = 50
    draw.rounded_rectangle(
        [display_x, display_y, display_x + display_w, display_y + display_h],
        radius=8,
        fill=(245, 230, 240, 255)
    )
    
    # Botones - Fila 1
    button_y = calc_y + 75
    button_h = 25
    button_spacing = 5
    
    # C
    draw.rounded_rectangle([calc_x + 15, button_y, calc_x + 50, button_y + button_h], 
                          radius=6, fill=(212, 165, 212, 255))
    # ÷
    draw.rounded_rectangle([calc_x + 55, button_y, calc_x + 90, button_y + button_h], 
                          radius=6, fill=(212, 165, 212, 255))
    # ×
    draw.rounded_rectangle([calc_x + 95, button_y, calc_x + 130, button_y + button_h], 
                          radius=6, fill=(244, 166, 215, 255))
    # -
    draw.rounded_rectangle([calc_x + 135, button_y, calc_x + 165, button_y + button_h], 
                          radius=6, fill=(244, 166, 215, 255))
    
    # Botones - Fila 2
    button_y += button_h + button_spacing
    # 7, 8, 9
    for i in range(3):
        x = calc_x + 15 + i * 40
        draw.rounded_rectangle([x, button_y, x + 35, button_y + button_h], 
                              radius=6, fill=(230, 208, 230, 255))
    # +
    draw.rounded_rectangle([calc_x + 135, button_y, calc_x + 165, button_y + button_h + 30], 
                          radius=6, fill=(244, 166, 215, 255))
    
    # Botones - Fila 3
    button_y += button_h + button_spacing
    # 4, 5, 6
    for i in range(3):
        x = calc_x + 15 + i * 40
        draw.rounded_rectangle([x, button_y, x + 35, button_y + button_h], 
                              radius=6, fill=(230, 208, 230, 255))
    
    # Botones - Fila 4
    button_y += button_h + button_spacing
    # 1, 2, 3
    for i in range(3):
        x = calc_x + 15 + i * 40
        draw.rounded_rectangle([x, button_y, x + 35, button_y + button_h], 
                              radius=6, fill=(230, 208, 230, 255))
    # =
    draw.rounded_rectangle([calc_x + 135, button_y, calc_x + 165, button_y + button_h], 
                          radius=6, fill=(240, 98, 146, 255))
    
    # Brillo/Highlight
    draw.ellipse([40, 30, 120, 90], fill=(255, 255, 255, 38))
    
    # Crear diferentes tamaños
    sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
    images = []
    
    for s in sizes:
        if s != (256, 256):
            resized = img.resize(s, Image.Resampling.LANCZOS)
            images.append(resized)
        else:
            images.append(img)
    
    # Guardar como ICO
    images[0].save('icono.ico', format='ICO', 
                   sizes=[(img.width, img.height) for img in images])
    
    print("Icono creado exitosamente: icono.ico")
    return True

if __name__ == "__main__":
    try:
        crear_icono()
    except Exception as e:
        print(f"Error: {e}")
