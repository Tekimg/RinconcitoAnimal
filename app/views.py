from django.shortcuts import render
from .models import User
from .forms import RegistrarForm


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
    if request.method is not "POST":
        usuarios = User.objects.all()
        context= {'usuarios':usuarios}
        return render(request,'app/registro.html', context)
    else:
        nombres = request.POST["nombres"]
        apellidos = request.POST["apellidos"]
        celular = request.POST["celular"]
        rut = request.POST["rut"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        
        obj=User.objects.create(
            nombres=nombres,
            apellidos=apellidos,
            celular=celular,
            rut=rut,
            email=email,
            pass1=pass1,
            pass2=pass2
        )
        obj.save()
        context={'mensaje':"Usuario registrado"}
        return render(request,'app/registro.html', context)