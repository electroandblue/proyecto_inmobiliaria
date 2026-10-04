from django.contrib import admin
from django.urls import path
from inmuebles_app import views

urlpatterns = [
    # Panel de administración
    path('admin/', admin.site.urls),

    # Requerimiento 3.a: Ruta para ver la oferta disponible
    path('', views.home, name='home'),

    # Autenticación y Perfil
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil, name='perfil'),

    # Requerimiento 1.a: Ruta para agregar un nuevo inmueble
    path('inmuebles/crear/', views.inmueble_crear, name='inmueble_crear'),

    # Requerimiento 2.a: Rutas para actualizar y eliminar inmuebles
    path('inmuebles/<int:pk>/editar/', views.inmueble_editar, name='inmueble_editar'),
    path('inmuebles/<int:pk>/eliminar/', views.inmueble_eliminar, name='inmueble_eliminar'),
]