from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ModificarDatosUsuarioForm, InmuebleForm
from .models import Inmueble

# ==========================================
# REQUERIMIENTO 3: OFERTA DISPONIBLE
# ==========================================
def home(request):
    """3.b: Lista toda la oferta disponible mediante el ORM"""
    inmuebles = Inmueble.objects.all()
    return render(request, 'inmuebles/lista_inmuebles.html', {'inmuebles': inmuebles})


# ==========================================
# AUTENTICACIÓN Y PERFIL DE USUARIO
# ==========================================
def registro(request):
    """Registro de nuevos usuarios"""
    if request.user.is_authenticated:
        return redirect('perfil')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Cuenta creada con éxito!')
            return redirect('perfil')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

def login_view(request):
    """Inicio de sesión"""
    if request.user.is_authenticated:
        return redirect('perfil')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bienvenido/a, {user.username}.')
            return redirect('perfil')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    """Cierre de sesión"""
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('home')

@login_required
def perfil(request):
    """Muestra datos del usuario y permite gestionar inmuebles existentes"""
    if request.method == 'POST':
        form = ModificarDatosUsuarioForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tus datos personales se han actualizado correctamente.')
            return redirect('perfil')
    else:
        form = ModificarDatosUsuarioForm(instance=request.user)

    # Recupera todos los inmuebles de la base de datos para la gestión
    mis_inmuebles = Inmueble.objects.all()

    return render(request, 'perfil.html', {
        'form': form,
        'mis_inmuebles': mis_inmuebles
    })


# ==========================================
# REQUERIMIENTO 1: AGREGAR NUEVO INMUEBLE
# ==========================================
@login_required
def inmueble_crear(request):
    """1.c: Guarda un nuevo inmueble en la base de datos usando el ORM"""
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save()
            messages.success(request, f"El inmueble '{inmueble.nombre}' se ha publicado con éxito.")
            return redirect('perfil')
    else:
        form = InmuebleForm()

    return render(request, 'inmuebles/inmueble_form.html', {
        'form': form,
        'titulo': 'Publicar Nuevo Inmueble'
    })


# ==========================================
# REQUERIMIENTO 2: ACTUALIZAR Y BORRAR INMUEBLE
# ==========================================
@login_required
def inmueble_editar(request, pk):
    """2.c: Actualiza un inmueble existente usando el ORM"""
    inmueble = get_object_or_404(Inmueble, pk=pk)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            messages.success(request, f"El inmueble '{inmueble.nombre}' se ha actualizado correctamente.")
            return redirect('perfil')
    else:
        form = InmuebleForm(instance=inmueble)

    return render(request, 'inmuebles/inmueble_form.html', {
        'form': form,
        'titulo': f'Editar Inmueble: {inmueble.nombre}'
    })

@login_required
def inmueble_eliminar(request, pk):
    """2.c: Elimina un inmueble de la base de datos usando el ORM"""
    inmueble = get_object_or_404(Inmueble, pk=pk)
    if request.method == 'POST':
        nombre = inmueble.nombre
        inmueble.delete()
        messages.success(request, f"El inmueble '{nombre}' ha sido eliminado.")
        return redirect('perfil')

    return render(request, 'inmuebles/inmueble_confirm_delete.html', {'inmueble': inmueble})