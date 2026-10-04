"""
Módulo de servicios CRUD para la gestión de inmuebles.
Requerimiento 3 del Hito 1: Operaciones en los modelos de Django.
"""
from inmuebles_app.models import Inmueble, TipoInmueble

# a. Crear un objeto con el modelo
def crear_inmueble(nombre, descripcion, direccion, precio, tipo_inmueble_id, m2=50, hab=1, banos=1):
    """Crea y guarda un nuevo inmueble en la base de datos."""
    try:
        tipo = TipoInmueble.objects.get(id=tipo_inmueble_id)
        inmueble = Inmueble.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            direccion=direccion,
            precio=precio,
            tipo_inmueble=tipo,
            m2_construidos=m2,
            habitaciones=hab,
            banos=banos
        )
        print(f"Inmueble creado con éxito: {inmueble.nombre} (ID: {inmueble.id})")
        return inmueble
    except Exception as e:
        print(f"Error al crear el inmueble: {e}")
        return None


# b. Enlistar desde el modelo de datos
def listar_inmuebles():
    """Retorna e imprime todos los inmuebles registrados en la base de datos."""
    inmuebles = Inmueble.objects.all()
    print(f"\n--- LISTADO DE INMUEBLES ({inmuebles.count()} encontrados) ---")
    for item in inmuebles:
        print(f"ID: {item.id} | {item.nombre} | Tipo: {item.tipo_inmueble.nombre} | Precio: ${item.precio}")
    return inmuebles


# c. Actualizar un registro en el modelo de datos
def actualizar_inmueble(inmueble_id, nuevo_precio=None, nueva_direccion=None):
    """Actualiza los datos de un inmueble existente."""
    try:
        inmueble = Inmueble.objects.get(id=inmueble_id)
        if nuevo_precio is not None:
            inmueble.precio = nuevo_precio
        if nueva_direccion is not None:
            inmueble.direccion = nueva_direccion
        inmueble.save()
        print(f"Inmueble ID {inmueble.id} actualizado correctamente.")
        return inmueble
    except Inmueble.DoesNotExist:
        print(f"El inmueble con ID {inmueble_id} no existe.")
        return None
    except Exception as e:
        print(f"Error al actualizar el inmueble: {e}")
        return None


# d. Borrar un registro del modelo de datos
def borrar_inmueble(inmueble_id):
    """Elimina un inmueble por su ID."""
    try:
        inmueble = Inmueble.objects.get(id=inmueble_id)
        nombre = inmueble.nombre
        inmueble.delete()
        print(f"Inmueble '{nombre}' (ID: {inmueble_id}) eliminado con éxito.")
        return True
    except Inmueble.DoesNotExist:
        print(f"El inmueble con ID {inmueble_id} no existe.")
        return False
    except Exception as e:
        print(f"Error al borrar el inmueble: {e}")
        return False