import json
import os

# Asegurar que exista la carpeta para guardar las páginas
os.makedirs("paginas_web", exist_ok=True)

# Leer la base de datos enriquecida
with open("data.json", "r", encoding="utf-8") as f:
    telefonos = json.load(f)

# Plantilla base en HTML
html_template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>¿El {modelo} sirve para jugar? Análisis Técnico Completo</title>
</head>
<body>
    <h1>Análisis de Rendimiento: {modelo} de {marca}</h1>
    <p>Si estás pensando en adquirir el <strong>{modelo}</strong> en Colombia (con un precio estimado de ${precio_co:,} COP), evaluar su hardware es vital antes de realizar la inversión. En esta guía desglosamos si su configuración técnica es capaz de soportar jornadas intensas de juego.</p>
    
    <h2>Especificaciones de Hardware Core</h2>
    <ul>
        <li><strong>Procesador:</strong> {procesador}</li>
        <li><strong>Memoria RAM:</strong> {ram} GB</li>
        <li><strong>Batería:</strong> {bateria} mAh con carga rápida de {carga_rapida}W</li>
        <li><strong>Pantalla:</strong> Tasa de refresco de {pantalla_hz}Hz</li>
    </ul>

    <h2>{titulo_potencia}</h2>
    <p>{analisis_potencia}</p>

    <h2>Rendimiento en Títulos Competitivos</h2>
    <h3>Free Fire</h3>
    <p>{rendimiento_free_fire}</p>
    
    <h3>Clash of Clans & Estrategia</h3>
    <p>{rendimiento_clash}</p>

    <h2>{titulo_autonomia}</h2>
    <p>{analisis_autonomia}</p>
</body>
</html>
"""

# Procesar cada teléfono y generar el contenido inteligente
for t in telefonos:
    # Lógica 1: Analizar la potencia por la combinación de RAM y Procesador
    if t["ram"] >= 12:
        titulo_potencia = "Rendimiento Gama Alta y Multitarea"
        analisis_potencia = f"El {t['modelo']} destaca notablemente gracias a sus {t['ram']} GB de memoria RAM combinados con el procesador {t['procesador']}. Esta configuración elimina cualquier cuello de botella, permitiendo mantener juegos pesados en segundo plano y asegurando que el sistema operativo no sufra ralentizaciones durante actualizaciones críticas."
    else:
        titulo_potencia = "Rendimiento Gama Media Balanceado"
        analisis_potencia = f"Equipado con {t['ram']} GB de RAM y el chip {t['procesador']}, el {t['modelo']} ofrece un comportamiento sólido para el día a día. Sin embargo, para sesiones de juego prolongadas, se recomienda cerrar aplicaciones en segundo plano para evitar que la gestión de memoria penalice los fotogramas por segundo (FPS)."

    # Lógica 2: Analizar la batería y el sistema de refrigeración
    if "Cámara de vapor" in t["refrigeracion"] or t["carga_rapida"] >= 60:
        titulo_autonomia = "Gestión Térmica Eficiente y Autonomía"
        analisis_autonomia = f"Un punto crítico para los jugadores es la temperatura. Este dispositivo cuenta con un sistema de '{t['refrigeracion']}', lo que mitiga el estrangulamiento térmico (thermal throttling). Además, su batería de {t['bateria']} mAh respaldada por una carga rápida de {t['carga_rapida']}W garantiza que podrás regresar a la partida en cuestión de minutos."
    else:
        titulo_autonomia = "Autonomía Estándar para Sesiones Moderadas"
        analisis_autonomia = f"Con una batería de {t['bateria']} mAh, el dispositivo cubre una jornada estándar de uso. No obstante, al contar con un sistema de refrigeración {t['refrigeracion']}, el calor generado tras un par de horas consecutivas de juego puede elevar la temperatura interna, reduciendo ligeramente la eficiencia de sus {t['carga_rapida']}W de carga."

    # Renderizar la plantilla con los datos duros y los textos generados por la IA del script
    html_final = html_template.format(
        modelo=t["modelo"],
        marca=t["marca"],
        precio_co=t["precio_co"],
        procesador=t["procesador"],
        ram=t["ram"],
        bateria=t["bateria"],
        carga_rapida=t["carga_rapida"],
        pantalla_hz=t["pantalla_hz"],
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

print("¡Fábrica de contenido optimizada! Páginas generadas con análisis profundo.")