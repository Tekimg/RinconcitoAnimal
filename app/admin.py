from django.contrib import admin
from .models import Producto, Categoria, User

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(User)
