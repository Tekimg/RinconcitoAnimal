from django import forms 
from .models import Categoria, Producto, User
from django.forms import ModelForm

class RegistrarForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"
