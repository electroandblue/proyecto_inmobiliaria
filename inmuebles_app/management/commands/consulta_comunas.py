from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Genera reporte de inmuebles para arriendo separados por comuna'

    def handle(self, *args, **kwargs):
        # Consulta SQL nativa que recupera comunas y solo nombre y descripción de los inmuebles
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

        self.stdout.write(self.style.SUCCESS(f"Reporte generado con éxito en '{nombre_archivo}'."))