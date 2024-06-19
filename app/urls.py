from django.urls import path
from . import views

urlpatterns = [
    path('home.html', views.home, name='home'),
    path('alimentos.html', views.alimentos, name='alimentos'),
    path('', views.inicio, name='inicio'),
    path('accesorios.html', views.accesorios, name='accesorios'),
]
