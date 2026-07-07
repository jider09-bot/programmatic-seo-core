import json
import os

def cargar_datos():
    with open('data.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def generar_paginas_web():
    dispositivos = cargar_datos()
    
    if not os.path.exists('paginas_web'):
        os.makedirs('paginas_web')
        
    print(f"🤖 Generando sitios web automatizados...")
    
    for disp in dispositivos:
        nombre_archivo = f"paginas_web/{disp['id']}.html"
        
        contenido_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rendimiento de {disp['marca']} {disp['modelo']} en Juegos</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f4f4f9; }}
        h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
        h2 {{ color: #2980b9; margin-top: 30px; }}
        .ficha {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
    </style>
</head>
<body>
    <h1>Análisis Técnico: {disp['marca']} {disp['modelo']} para Gaming</h1>
    <div class="ficha">
        <p><strong>Procesador:</strong> {disp['procesador']}</p>
        <p><strong>Pantalla:</strong> {disp['pantalla']}</p>
    </div>
    <h2>Rendimiento en Free Fire</h2>
    <p>{disp['rendimiento_free_fire']}</p>
    <h2>Rendimiento en Clash Royale</h2>
    <p>{disp['rendimiento_clash']}</p>
</body>
</html>
"""
        with open(nombre_archivo, 'w', encoding='utf-8') as file:
            file.write(contenido_html)
            
        print(f"✅ Página creada: {nombre_archivo}")

if __name__ == "__main__":
    generar_paginas_web()