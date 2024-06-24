from django.shortcuts import render

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
    return render(request, 'app/registro.html')