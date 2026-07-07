import json
import os

# Asegurar que exista la carpeta para guardar las páginas
os.makedirs("paginas_web", exist_ok=True)

# Leer la base de datos enriquecida
with open("data.json", "r", encoding="utf-8") as f:
    telefonos = json.load(f)

# DISEÑO VISUAL (CSS PREMIUM): Estilo Gaming / Dark Mode
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
    .container { max-width: 700px; margin: 0 auto; }
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
    .spec-card span { display: block; font-size: 0.85rem; color: var(--texto-secundario); uppercase; }
    .spec-card strong { font-size: 1.05rem; color: var(--texto-principal); }
    .game-box {
        background: #111827;
        padding: 20px;
        border-radius: 12px;
        margin-top: 15px;
        border: 1px solid rgba(255,255,255,0.05);
    }
    @media (max-width: 480px) {
        .specs-grid { grid-template-columns: 1fr; }
        h1 { font-size: 1.8rem; }
    }
"""

# PLANTILLA BASE EN HTML
html_template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>¿El {modelo} sirve para jugar? Análisis Técnico Completo</title>
    <style>
        {estilos_css}
    </style>
</head>
<body>
    <div class="container">
        <header>
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

# Procesar cada teléfono y generar el contenido inteligente
for t in telefonos:
    # Lógica 1: Analizar la potencia por la combinación de RAM y Procesador
    if t["ram"] >= 12:
        titulo_potencia = "Rendimiento Gama Alta y Multitarea"
        analisis_potencia = f"El {t['modelo']} destaca notablemente gracias a sus {t['ram']} GB de memoria RAM combinados con el procesador {t['procesador']}. Esta configuración elimina cualquier cuello de botella, permitiendo mantener juegos pesados en segundo plano y asegurando que el sistema operativo no sufra ralentizaciones durante actualizaciones críticas o partidas de alta exigencia gráfica."
    else:
        titulo_potencia = "Rendimiento Gama Media Balanceado"
        analisis_potencia = f"Equipado con {t['ram']} GB de RAM y el chip {t['procesador']}, el {t['modelo']} ofrece un comportamiento sólido para el día a día. Sin embargo, para sesiones de juego prolongadas en títulos competitivos, se recomienda cerrar aplicaciones en segundo plano para evitar que la gestión de memoria penalice los fotogramas por segundo (FPS)."

    # Lógica 2: Analizar la batería y el sistema de refrigeración
    if "Cámara de vapor" in t["refrigeracion"] or t["carga_rapida"] >= 60:
        titulo_autonomia = "Gestión Térmica Eficiente y Autonomía"
        analisis_autonomia = f"Un punto crítico para los jugadores es la temperatura. Este dispositivo cuenta con un sistema de '{t['refrigeracion']}', lo que mitiga el estrangulamiento térmico (thermal throttling). Además, su batería de {t['bateria']} mAh respaldada por una carga rápida de {t['carga_rapida']}W garantiza que podrás regresar a la partida en cuestión de minutos."
    else:
        titulo_autonomia = "Autonomía Estándar para Sesiones Moderadas"
        analisis_autonomia = f"Con una batería de {t['bateria']} mAh, el dispositivo cubre una jornada estándar de uso. No obstante, al contar con un sistema de refrigeración {t['refrigeracion']}, el calor generado tras un par de horas consecutivas de juego puede elevar la temperatura interna, reduciendo ligeramente la eficiencia de sus {t['carga_rapida']}W de carga."

    # Renderizar la plantilla inyectando el CSS y las variables del teléfono
    html_final = html_template.format(
        estilos_css=css_styles,
        modelo=t["modelo"],
        marca=t["marca"],
        precio_co=t["precio_co"],
        procesador=t["procesador"],
        ram=t["ram"],
        bateria=t["bateria"],
        carga_rapida=t["carga_rapida"],
        pantalla_hz=t["pantalla_hz"],
        refrigeracion=t["refrigeracion"],
        titulo_potencia=titulo_potencia,
        analisis_potencia=analisis_potencia,
        rendimiento_free_fire=t["rendimiento_free_fire"],
        rendimiento_clash=t["rendimiento_clash"],
        titulo_autonomia=titulo_autonomia,
        analisis_autonomia=analisis_autonomia
    )

    # Guardar el archivo HTML generado
    file_name = f"paginas_web/{t['id']}.html"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(html_final)

print("¡Fábrica actualizada con Diseño Premium Dark Mode!")