import json
import os
from datetime import datetime

# Asegurar que exista la carpeta para guardar las páginas hijas
os.makedirs("paginas_web", exist_ok=True)

# Leer la base de datos enriquecida
with open("data.json", "r", encoding="utf-8") as f:
    telefonos = json.load(f)

# Tu URL base de GitHub Pages (Para el mapa del sitio)
URL_BASE = "https://jider09-bot.github.io/programmatic-seo-core"

# Estilos CSS compartidos para todo el sitio
css_styles = """
    :root {
        --bg-principal: #0f172a;
        --bg-tarjeta: #1e293b;
        --texto-principal: #f8fafc;
        --texto-secundario: #94a3b8;
        --acentos: #38bdf8;
        --exito: #4ade80;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { 
        font-family: 'Segoe UI', system-ui, sans-serif; 
        background-color: var(--bg-principal); 
        color: var(--texto-principal); 
        line-height: 1.6;
        padding: 20px;
    }
    .container { max-width: 800px; margin: 0 auto; }
    header { text-align: center; padding: 40px 0 20px 0; }
    h1 { font-size: 2.2rem; color: var(--texto-principal); margin-bottom: 10px; line-height: 1.2; }
    .badge-precio { 
        display: inline-block; 
        background: rgba(56, 189, 248, 0.1); 
        color: var(--acentos); 
        padding: 6px 16px; 
        border-radius: 20px; 
        font-weight: bold; 
        font-size: 0.9rem;
    }
    .intro { color: var(--texto-secundario); font-size: 1.1rem; margin: 25px 0; text-align: justify; }
    h2 { font-size: 1.4rem; color: var(--acentos); margin: 35px 0 15px 0; border-bottom: 1px solid var(--bg-tarjeta); padding-bottom: 8px; }
    h3 { font-size: 1.1rem; color: var(--texto-principal); margin: 15px 0 5px 0; display: flex; align-items: center; }
    p { color: var(--texto-secundario); margin-bottom: 15px; text-align: justify; }
    
    .specs-grid { 
        display: grid; 
        grid-template-columns: repeat(2, 1fr); 
        gap: 15px; 
        margin: 20px 0; 
    }
    .spec-card { 
        background: var(--bg-tarjeta); 
        padding: 15px; 
        border-radius: 12px; 
        border-left: 4px solid var(--acentos);
    }
    .spec-card span { display: block; font-size: 0.85rem; color: var(--texto-secundario); text-transform: uppercase; }
    .spec-card strong { font-size: 1.05rem; color: var(--texto-principal); }
    
    .game-box {
        background: #111827;
        padding: 20px;
        border-radius: 12px;
        margin-top: 15px;
        border: 1px solid rgba(255,255,255,0.05);
    }
    
    .grid-portal {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
        margin-top: 30px;
    }
    .card-portal {
        background: var(--bg-tarjeta);
        padding: 25px;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.05);
        transition: transform 0.2s, border-color 0.2s;
        text-decoration: none;
        display: block;
    }
    .card-portal:hover {
        transform: translateY(-5px);
        border-color: var(--acentos);
    }
    .card-portal h2 {
        margin: 0 0 10px 0;
        border: none;
        padding: 0;
        color: var(--texto-principal);
    }
    .card-portal .detalles {
        font-size: 0.9rem;
        color: var(--texto-secundario);
    }
    .btn-leer {
        margin-top: 15px;
        color: var(--acentos);
        font-weight: bold;
        font-size: 0.95rem;
    }

    @media (max-width: 600px) {
        .specs-grid, .grid-portal { grid-template-columns: 1fr; }
        h1 { font-size: 1.8rem; }
    }
"""

# PLANTILLA PARA LAS PÁGINAS INDIVIDUALES (CON META TAGS SEO)
html_template_hija = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>¿El {modelo} sirve para jugar? Análisis Técnico Completo</title>
    <meta name="description" content="{meta_descripcion}">
    <meta name="keywords" content="{modelo} gaming, {modelo} free fire, rendimiento {modelo}, precio {modelo} colombia">
    <meta name="robots" content="index, follow">
    
    <style>{estilos_css}</style>
</head>
<body>
    <div class="container">
        <header>
            <a href="../index.html" style="color: var(--acentos); text-decoration: none; font-size: 0.9rem; float: left;">← Volver al Inicio</a>
            <br><br>
            <h1>Análisis de Rendimiento:<br>{modelo}</h1>
            <div class="badge-precio">Precio aprox: ${precio_co:,} COP</div>
        </header>
        
        <p class="intro">Si estás pensando en adquirir el <strong>{modelo}</strong> de {marca} en Colombia, evaluar su hardware a fondo es vital antes de realizar la inversión. En esta guía desglosamos si su configuración técnica es capaz de soportar jornadas intensas de juego sin caídas de frames.</p>
        
        <h2>Especificaciones de Hardware Core</h2>
        <div class="specs-grid">
            <div class="spec-card"><span>Procesador</span><strong>{procesador}</strong></div>
            <div class="spec-card"><span>Memoria RAM</span><strong>{ram} GB</strong></div>
            <div class="spec-card"><span>Batería</span><strong>{bateria} mAh</strong></div>
            <div class="spec-card"><span>Carga Rápida</span><strong>{carga_rapida}W</strong></div>
            <div class="spec-card"><span>Tasa de Refresco</span><strong>{pantalla_hz}Hz</strong></div>
            <div class="spec-card"><span>Refrigeración</span><strong>{refrigeracion}</strong></div>
        </div>

        <h2>{titulo_potencia}</h2>
        <p>{analisis_potencia}</p>

        <h2>Comportamiento en Títulos Competitivos</h2>
        <div class="game-box">
            <h3>🔥 Free Fire</h3>
            <p>{rendimiento_free_fire}</p>
            
            <h3>👑 Clash of Clans</h3>
            <p>{rendimiento_clash}</p>
        </div>

        <h2>{titulo_autonomia}</h2>
        <p>{analisis_autonomia}</p>
    </div>
</body>
</html>
"""

items_home_html = ""
urls_sitemap = []

hoy = datetime.today().strftime('%Y-%m-%d')
urls_sitemap.append(f"    <url>\n        <loc>{URL_BASE}/index.html</loc>\n        <lastmod>{hoy}</lastmod>\n        <priority>1.0</priority>\n    </url>")

# 1. Procesar cada teléfono y generar el contenido
for t in telefonos:
    if t["ram"] >= 12:
        titulo_potencia = "Rendimiento Gama Alta y Multitarea"
        analisis_potencia = f"El {t['modelo']} destaca notablemente gracias a sus {t['ram']} GB de memoria RAM combinados con el procesador {t['procesador']}. Esta configuración elimina cualquier cuello de botella, permitiendo mantener juegos pesados en segundo plano y asegurando estabilidad total."
    else:
        titulo_potencia = "Rendimiento Gama Media Balanceado"
        analisis_potencia = f"Equipado con {t['ram']} GB de RAM y el chip {t['procesador']}, el {t['modelo']} ofrece un comportamiento sólido para el día a día. Sin embargo, para sesiones prolongadas, se recomienda cerrar aplicaciones en segundo plano."

    if "Cámara de vapor" in t["refrigeracion"] or t["carga_rapida"] >= 60:
        titulo_autonomia = "Gestión Térmica Eficiente y Autonomía"
        analisis_autonomia = f"Este dispositivo cuenta con un sistema de '{t['refrigeracion']}', lo que mitiga el estrangulamiento térmico (thermal throttling). Además, su batería de {t['bateria']} mAh respaldada por una carga rápida de {t['carga_rapida']}W garantiza regresar a la acción rápido."
    else:
        titulo_autonomia = "Autonomía Estándar para Sesiones Moderadas"
        analisis_autonomia = f"Con una batería de {t['bateria']} mAh, el dispositivo cubre una jornada estándar de uso. No obstante, al contar con refrigeración {t['refrigeracion']}, el calor tras un par de horas continuas de juego puede reducir ligeramente el rendimiento óptimo."

    meta_desc = f"Análisis técnico del {t['modelo']} para gaming en Colombia. Descubre si sus {t['ram']}GB de RAM y procesador {t['procesador']} corren Free Fire sin lag."

    # RENDERIZADO CORREGIDO: 'refrigeracion' en lugar de 'refrigeration'
    html_final = html_template_hija.format(
        estilos_css=css_styles, modelo=t["modelo"], marca=t["marca"], precio_co=t["precio_co"],
        procesador=t["procesador"], ram=t["ram"], bateria=t["bateria"], carga_rapida=t["carga_rapida"],
        pantalla_hz=t["pantalla_hz"], refrigeracion=t["refrigeracion"], titulo_potencia=titulo_potencia,
        analisis_potencia=analisis_potencia, rendimiento_free_fire=t["rendimiento_free_fire"],
        rendimiento_clash=t["rendimiento_clash"], titulo_autonomia=titulo_autonomia, 
        analisis_autonomia=analisis_autonomia, meta_descripcion=meta_desc
    )

    with open(f"paginas_web/{t['id']}.html", "w", encoding="utf-8") as f:
        f.write(html_final)

    items_home_html += f"""
        <a href="paginas_web/{t['id']}.html" class="card-portal">
            <h2>{t['modelo']}</h2>
            <div class="detalles">Procesador: {t['procesador']} | RAM: {t['ram']}GB</div>
            <div class="btn-leer">Ver Análisis Gaming →</div>
        </a>
    """

    urls_sitemap.append(f"    <url>\n        <loc>{URL_BASE}/paginas_web/{t['id']}.html</loc>\n        <lastmod>{hoy}</lastmod>\n        <priority>0.8</priority>\n    </url>")

# 2. GENERAR LA PÁGINA DE INICIO (INDEX.HTML)
html_template_home = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GamingTech Hub - Análisis de Rendimiento Móvil</title>
    <meta name="description" content="¿Qué tan bien rinde tu próximo teléfono? Evaluamos hardware en Colombia para juegos competitivos como Free Fire y Clash of Clans.">
    <style>{css_styles}</style>
</head>
<body>
    <div class="container">
        <header>
            <h1>GamingTech Hub</h1>
            <p style="color: var(--acentos); font-weight: bold;">¿Qué tan bien rinde tu próximo teléfono?</p>
        </header>
        
        <p class="intro" style="text-align: center;">Bienvenido al portal de pruebas técnicas. Analizamos el hardware de los smartphones más populares en Colombia para determinar si son capaces de mantener los FPS estables en títulos exigentes.</p>
        
        <h2>Dispositivos Analizados Recientemente</h2>
        <div class="grid-portal">
            {items_home_html}
        </div>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template_home)

# 3. CONSTRUIR E INYECTAR EL SITEMAP.XML AUTOMÁTICO
sitemap_xml_final = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls_sitemap)}
</urlset>
"""

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_xml_final)

print("¡Ecosistema optimizado! Páginas, Index y Sitemap.xml creados exitosamente.")