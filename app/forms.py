from django import forms 
from .models import Categoria, Producto, User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class RegistroUserForm(UserCreationForm):
    pass
class RegistrarForm(ModelForm):
    class Meta: 
        model = User
        fields = [ 'rut', 'nombres', 'apellidos', 'celular', 'email', 'pass1', 'pass2']
        labels = {
            'rut':'Rut (12345678-0)',
            'nombres':'Nombres:',
            'apellidos':'Apellidos:',
            'celular':'Celular (+56 9):',
            'email':'Email',
            'pass1':'Contraseña',
            'pass2':'Confirmar contraseña',
            }
        widgets = {
            'rut': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese su rut...',
                    'id': 'rut',
                    'class': 'form-control'
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre...',
                    'id': 'nombres',
                    'class': 'form-control'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su apellido...',
                    'id': 'apellidos',
                    'class': 'form-control'
                }
            ),
            'celular': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su celular...',
                    'id': 'celular',
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Ingrese su email...',
                    'id': 'email',
                    'class': 'form-control'
                }
            ),
            'pass1': forms.PasswordInput(
                attrs={
                    'placeholder': 'Ingrese una contraseña...',
                    'id': 'pass1',
                    'class': 'form-control'
                }
            ),
            'pass2': forms.PasswordInput(
                attrs={
                    'placeholder': 'Ingrese su contraseña nuevamente...',
                    'id': 'pass2',
                    'class': 'form-control'
                }
            ),
        }
        