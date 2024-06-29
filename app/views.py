from django.shortcuts import render, redirect
from .models import User
from .forms import RegistrarForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Producto, Categoria


# Create your views here.
def inicio(request):
    return render(request, 'app/inicio.html')

def home(request):
    return render(request, 'app/home.html')

def alimentos(request):
    categoria = Categoria.objects.get(nom_categoria='Alimentos')
    products = Producto.objects.filter(id_categoria=categoria)[:8]
    return render(request, 'app/alimentos.html', {'products':products})


def accesorios(request):
    categoria = Categoria.objects.get(nom_categoria='Accesorios')
    products = Producto.objects.filter(id_categoria=categoria)[:8]
    return render(request, 'app/accesorios.html', {'products':products})

def farmacia(request):
    categoria = Categoria.objects.get(nom_categoria='Farmacia')
    products = Producto.objects.filter(id_categoria=categoria)[:8]
    return render(request, 'app/farmacia.html', {'products':products})

def login(request):
    return render(request, 'app/login.html')

def registro(request):
    mensaje = ''  
    if request.method == 'POST':
        form = RegistrarForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = 'Usuario registrado correctamente.'
            return render(request, 'app/login.html', {'mensaje': mensaje})
    else:
        form = RegistrarForm()

    return render(request, 'app/registro.html', {'registrarForm': form, 'mensaje_error': mensaje})
