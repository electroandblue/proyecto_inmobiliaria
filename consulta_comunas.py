import os
import sys
from pathlib import Path
import django

# Asegurar que la raíz del proyecto esté en sys.path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_inmobiliaria.settings')
django.setup()

from django.db import connection

def consultar_inmuebles_por_comuna():
    # Consulta SQL nativa que une comunas e inmuebles seleccionando solo nombre y descripción
    query = """
        SELECT c.nombre AS comuna, i.nombre AS inmueble, i.descripcion
        FROM inmuebles_app_inmueble i
        INNER JOIN inmuebles_app_comuna c ON i.comuna_id = c.id
        ORDER BY c.nombre, i.nombre;
    """
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        filas = cursor.fetchall()

    # Agrupar los resultados por comuna
    comunas_dict = {}
    for comuna, inmueble_nombre, inmueble_desc in filas:
        if comuna not in comunas_dict:
            comunas_dict[comuna] = []
        comunas_dict[comuna].append((inmueble_nombre, inmueble_desc))

    # Guardar en archivo de texto según la rúbrica
    nombre_archivo = "inmuebles_por_comuna.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("============================================================\n")
        f.write("LISTADO DE INMUEBLES PARA ARRIENDO SEPARADO POR COMUNAS\n")
        f.write("============================================================\n\n")
        
        for comuna, propiedades in comunas_dict.items():
            f.write(f"COMUNA: {comuna.upper()}\n")
            f.write("-" * 50 + "\n")
            for nombre, desc in propiedades:
                f.write(f"• Nombre: {nombre}\n")
                f.write(f"  Descripción: {desc}\n\n")
            f.write("\n")

    print(f"Reporte generado con éxito en '{nombre_archivo}'.")

if __name__ == '__main__':
    consultar_inmuebles_por_comuna()