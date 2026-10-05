# 🏢 Sistema de Gestión y Arriendo de Inmuebles
> Plataforma web integral para la administración, publicación y consulta territorial de propiedades habitacionales, construida bajo el patrón arquitectónico MVT con Django, base de datos relacional PostgreSQL y estilizado responsivo con Bootstrap 5.

---

## 📌 Descripción General
El proyecto consiste en una aplicación web desarrollada para optimizar el proceso de arriendo y administración de propiedades. La plataforma permite a los usuarios navegar por la oferta inmobiliaria disponible clasificada por región y comuna, registrarse e iniciar sesión de manera segura, y a los arrendadores gestionar el ciclo de vida completo de sus publicaciones (Crear, Consultar, Actualizar y Eliminar) mediante el ORM nativo de Django.

---

## 🛠️ Tecnologías y Entorno de Desarrollo
* **Lenguaje:** Python 3.10+
* **Framework Web:** Django 5.2+
* **Base de Datos:** PostgreSQL
* **Driver de Conexión:** psycopg2-binary
* **Frontend:** HTML5 semántico, CSS3, Bootstrap 5
* **Gestión de Entorno:** Python venv
* **Control de Versiones:** Git & GitHub

---

## 🏗️️ Arquitectura y Modelo Relacional
El sistema modela la integridad territorial y habitacional a través de cuatro entidades principales vinculadas mediante claves foráneas (`models.ForeignKey`):

1. **`Region`:** Representa la división político-administrativa territorial.
2. **`Comuna`:** Vinculada a una región mediante `region = models.ForeignKey(Region, on_delete=models.CASCADE)`.
3. **`TipoInmueble`:** Clasificación de la propiedad (Casa, Departamento, Parcela, Oficina, etc.).
4. **`Inmueble`:** Entidad central que almacena nombre, descripción, dirección, precio de arriendo, m² construidos, habitaciones, baños y su relación directa con `TipoInmueble` y `Comuna`.
5. [ Region ] 1 ───< N [ Comuna ] 1 ───< N [ Inmueble ] >─── 1 [ TipoInmueble ]
6. ## ✨ Funcionalidades Principales

### 1. Manipulación de Datos y Ciclo CRUD (ORM)
* **Creación:** Formulario interactivo (`InmuebleForm`) para la publicación de nuevas propiedades con validación de datos.
* **Lectura y Catálogo:** Despliegue de tarjetas responsivas en la página principal (`/`) con la oferta de viviendas activas.
* **Actualización:** Edición contextual de propiedades desde el panel de usuario (`/perfil/`).
* **Eliminación:** Borrado seguro de registros en base de datos PostgreSQL con confirmación previa.

### 2. Autenticación y Perfil de Usuario
* Registro de usuarios mediante `UserCreationForm`.
* Vistas de acceso y salida (`LoginView`, `LogoutView`) con control de sesiones y redireccionamientos seguros.
* Panel privado (`/perfil/`) para visualizar credenciales del usuario y administrar sus propiedades publicadas.

### 3. Comandos Personalizados de Reportes SQL (`management/commands`)
El sistema integra comandos CLI ejecutables vía `manage.py` que utilizan consultas SQL directas (`django.db.connection`) para auditoría y reportería:
* `python manage.py consulta_comunas`: Exporta las propiedades agrupadas por comuna en `inmuebles_por_comuna.txt`.
* `python manage.py consulta_regiones`: Exporta el catálogo consolidado por regiones en `inmuebles_por_region.txt`.

### 4. Panel de Administración Personalizado (Django Admin)
* Modelos registrados con interfaces optimizadas (`ModelAdmin`).
* Filtros laterales (`list_filter`) por comuna, región y tipo de vivienda.
* Búsqueda en tiempo real (`search_fields`) por título, dirección y descripción.

---

## 🚀 Instalación y Puesta en Marcha

### 1. Clonar el repositorio
```bash
git clone [https://github.com/electroandblue/proyecto_inmobiliaria.git](https://github.com/electroandblue/proyecto_inmobiliaria.git)
cd proyecto_inmobiliaria
2. Configurar el entorno virtual
Bash
python -m venv env
# En Windows:
.\env\Scripts\activate
# En Linux/Mac:
source env/bin/activate
3. Instalar dependencias
Bash
pip install django psycopg2-binary
4. Configurar variables de base de datos
Configurar las credenciales locales de PostgreSQL en sistema_arriendo/settings.py (o variables de entorno):

Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'inmobiliaria_db',
        'USER': 'postgres',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
5. Aplicar migraciones y cargar fixtures
Bash
python manage.py migrate
python manage.py loaddata tipos_inmuebles.json
python manage.py loaddata inmuebles_usuarios.json
6. Ejecutar el servidor local
Bash
python manage.py runserver
Acceder a la aplicación desde el navegador en http://127.0.0.1:8000/.
👤 Autora
Constanza Mena - Licenciada en Marketing Digital | Fullstack Python Trainee
GitHub: @electroandblue
LinkedIn: Constanza Mena
