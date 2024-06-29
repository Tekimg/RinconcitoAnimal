from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import   RegistroUserForm
from .forms import ProductoForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
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

def user_login(request):
    return render(request, 'registration/login.html')


@login_required
def editarProductos(request):
    return render(request, 'app/editarProductos.html')


def registro(request):
    data = {
        'form': RegistroUserForm()
    }

    if request.method == 'POST':
        user_creation_form = RegistroUserForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'],
                                password=user_creation_form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                return redirect('home')
    
    return render(request, 'registration/registro.html', data)




def salir(request):
    logout(request)
    return redirect('home')


# Vista para listar productos
@login_required
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'app/producto_list.html', {'productos': productos})


# Vista para crear un nuevo producto
@login_required
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'app/producto_form.html', {'form': form})

# Vista para actualizar un producto existente
@login_required
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'app/producto_form.html', {'form': form})

# Vista para eliminar un producto
@login_required
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'app/producto_confirm_delete.html', {'producto': producto})