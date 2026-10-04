# Proyecto: Manejo del CRUD - Hito 1

**Programa:** Desarrollo de Aplicaciones Fullstack Python Trainee (SENCE / Desafío Latam)  
**Proyecto:** Sistema de Arriendo de Inmuebles  

---

## 1. Descripción del Proyecto

El proyecto consiste en el desarrollo del backend inicial para una plataforma web dedicada a la publicación y gestión de arriendo de inmuebles. En este primer hito se configuró el entorno de desarrollo, la conexión a una base de datos relacional PostgreSQL, el diseño y modelado de datos mediante claves foráneas con el ORM de Django, y la implementación de las operaciones CRUD (Crear, Leer, Actualizar y Borrar).

---

## 2. Entorno y Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Framework:** Django 5.2+
* **Base de Datos:** PostgreSQL
* **Conector:** psycopg2-binary
* **Entorno Virtual:** venv

---

## 3. Configuración y Conexión a la Base de Datos

En el archivo `sistema_arriendo/settings.py` se parametrizó la conexión a PostgreSQL con las credenciales locales:

* **ENGINE:** `django.db.backends.postgresql`
* **NAME:** `inmobiliaria_db`
* **USER:** `postgres`
* **HOST:** `localhost`
* **PORT:** `5432`

---

## 4. Modelos de Datos y Relaciones (ORM)

Dentro de la aplicación `inmuebles_app`, en el archivo `models.py`, se implementaron dos entidades principales relacionadas mediante una clave foránea:

1. **`TipoInmueble`:** Representa la categoría del inmueble (Casa, Departamento, etc.).
2. **`Inmueble`:** Contiene los atributos de la propiedad (nombre, descripción, dirección, precio, m2 construidos, habitaciones, baños) y la clave foránea:
   ```python
   tipo_inmueble = models.ForeignKey(TipoInmueble, on_delete=models.CASCADE, related_name='inmuebles')
   ```

Las migraciones fueron generadas y aplicadas a PostgreSQL exitosamente mediante:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5. Implementación de Operaciones CRUD

Las operaciones de manipulación de datos requeridas fueron implementadas en el módulo `inmuebles_app/services.py`:

* **a. Crear (`crear_inmueble`):** Valida la existencia del tipo de inmueble asociado y genera un nuevo registro persistente utilizando `Inmueble.objects.create(...)`.
* **b. Enlistar (`listar_inmuebles`):** Recupera e imprime todas las instancias registradas con `Inmueble.objects.all()`.
* **c. Actualizar (`actualizar_inmueble`):** Permite modificar campos específicos (como precio o dirección) y persistir el cambio mediante el método `.save()`.
* **d. Borrar (`borrar_inmueble`):** Localiza el registro correspondiente mediante su ID y procede con su eliminación de la base de datos a través de `.delete()`.

Todas las funciones fueron probadas y verificadas directamente en el shell interactivo de Django:

```bash
python manage.py shell
```