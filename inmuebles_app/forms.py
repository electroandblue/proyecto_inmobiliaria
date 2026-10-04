from django import forms
from django.contrib.auth.models import User
from .models import Inmueble

class ModificarDatosUsuarioForm(forms.ModelForm):
    """Formulario para que Arrendatarios y Arrendadores modifiquen sus datos personales"""
    first_name = forms.CharField(label="Nombre", max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Apellido", max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Correo Electrónico", required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class InmuebleForm(forms.ModelForm):
    """Formulario adaptado exactamente a los campos existentes en el modelo Inmueble"""
    class Meta:
        model = Inmueble
        fields = [
            'nombre',
            'descripcion',
            'direccion',
            'precio',
            'm2_construidos',
            'habitaciones',
            'banos',
            'tipo_inmueble',
            'comuna',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Departamento Centro'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del inmueble'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección completa'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio en CLP'}),
            'm2_construidos': forms.NumberInput(attrs={'class': 'form-control'}),
            'habitaciones': forms.NumberInput(attrs={'class': 'form-control'}),
            'banos': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_inmueble': forms.Select(attrs={'class': 'form-select'}),
            'comuna': forms.Select(attrs={'class': 'form-select'}),
        }