from django.urls import path, include
from . import views
from .views import producto_list, producto_create, producto_update, producto_delete


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('home.html', views.home, name='home'),
    path('alimentos.html', views.alimentos, name='alimentos'),
    path('accesorios.html', views.accesorios, name='accesorios'),
    path('farmacia.html', views.farmacia, name='farmacia'),
    path('registration/login.html', views.user_login, name='login'),
    path('registro', views.registro, name='registro'),
    path('editarProductos.html', views.editarProductos, name='editarProductos'),

     # Nuevas URLs para las vistas CRUD de Producto
    path('productos/', producto_list, name='producto_list'),
    path('productos/new/', producto_create, name='producto_create'),
    path('productos/<int:pk>/edit/', producto_update, name='producto_update'),
    path('productos/<int:pk>/delete/', producto_delete, name='producto_delete'),


    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/',views.salir,name="salir")
]



