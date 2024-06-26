from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('home.html', views.home, name='home'),
    path('alimentos.html', views.alimentos, name='alimentos'),
    path('accesorios.html', views.accesorios, name='accesorios'),
    path('farmacia.html', views.farmacia, name='farmacia'),
    path('login.html', views.login, name='login'),
    path('registro.html', views.registro, name='registro'),

]
