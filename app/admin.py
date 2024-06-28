from django.contrib import admin
from .models import Producto, Categoria, User, Order

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(User)
admin.site.register(Order) 