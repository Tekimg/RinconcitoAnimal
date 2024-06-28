from django.shortcuts import render, redirect
from .models import User
from .forms import RegistrarForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def inicio(request):
    return render(request, 'app/inicio.html')

def home(request):
    return render(request, 'app/home.html')

def alimentos(request):
    return render(request, 'app/alimentos.html')

def accesorios(request):
    return render(request, 'app/accesorios.html')

def farmacia(request):
    return render(request, 'app/farmacia.html')

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
