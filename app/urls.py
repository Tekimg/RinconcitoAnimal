from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('home.html', views.home, name='home'),
    path('alimentos.html', views.alimentos, name='alimentos'),
    path('accesorios.html', views.accesorios, name='accesorios'),
    path('farmacia.html', views.farmacia, name='farmacia'),
    path('login.html', views.login, name='login'),
    path('registro.html', views.registro, name='registro'),
    path('editarProductos.html', views.editarProductos, name='editarProductos'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/',views.salir,name="salir")
]
