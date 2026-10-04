from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Genera reporte de inmuebles para arriendo separados por region'

    def handle(self, *args, **kwargs):
        # Consulta SQL nativa que une inmuebles, comunas y regiones
        query = """
            SELECT r.nombre AS region, i.nombre AS inmueble, i.descripcion, i.precio
            FROM inmuebles_app_inmueble i
            INNER JOIN inmuebles_app_comuna c ON i.comuna_id = c.id
            INNER JOIN inmuebles_app_region r ON c.region_id = r.id
            ORDER BY r.nombre, i.nombre;
        """
        
        with connection.cursor() as cursor:
            cursor.execute(query)
            filas = cursor.fetchall()

        # Agrupar los resultados por region
        regiones_dict = {}
        for region, inmueble_nombre, inmueble_desc, precio in filas:
            if region not in regiones_dict:
                regiones_dict[region] = []
            regiones_dict[region].append((inmueble_nombre, inmueble_desc, precio))

        # Guardar en archivo de texto según la rúbrica
        nombre_archivo = "inmuebles_por_region.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("============================================================\n")
            f.write("LISTADO DE INMUEBLES PARA ARRIENDO SEPARADO POR REGIONES\n")
            f.write("============================================================\n\n")
            
            for region, propiedades in regiones_dict.items():
                f.write(f"REGIÓN: {region.upper()}\n")
                f.write("-" * 50 + "\n")
                for nombre, desc, precio in propiedades:
                    f.write(f"• Inmueble: {nombre}\n")
                    f.write(f"  Descripción: {desc}\n")
                    f.write(f"  Precio Arriendo: ${precio}\n\n")
                f.write("\n")

        self.stdout.write(self.style.SUCCESS(f"Reporte generado con éxito en '{nombre_archivo}'."))