from django.db import models
#Regex para validar que tengan los formatos de registro
from django.core.validators import RegexValidator, EmailValidator
import datetime


# Create your models here.
class Producto(models.Model):
    id_producto =models.AutoField(db_column="id_producto", primary_key=True)
    id_categoria= models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='id_categoria')
    foto= models.ImageField('Imagen',upload_to='fotosProductos/',max_length=255,null=False, blank=True)
    nom_producto=models.CharField(max_length=200, blank=False, null=False)
    descripcion =models.TextField(max_length=500)
    cantidad=models.CharField(max_length=5, blank=False, null=False)
    precio =models.CharField(max_length=45, blank=False, null=False)

    def __str__(self):
        return self.nom_producto
    

class Categoria(models.Model):
    id_categoria =models.AutoField(db_column="id_categoria", primary_key=True)
    nom_categoria=models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return self.nom_categoria
    

class User(models.Model):
    rut_regex = RegexValidator(regex=r'^\d{7,8}-[0-9kK]{1}$', message="El RUT debe tener el formato: 12345678-0")
    rut = models.CharField(validators=[rut_regex], max_length=10, unique=True, verbose_name="RUT")
    nombres = models.CharField(max_length=30, verbose_name="Nombres")
    apellidos = models.CharField(max_length=30, verbose_name="Apellidos")
    cel_regex = RegexValidator(regex=r'^\+569\d{8}$', message="El número debe tener el formato: +569xxxxxxxx")
    celular = models.CharField(validators=[cel_regex], max_length=12, verbose_name="Teléfono")
    email = models.EmailField(validators=[EmailValidator()], unique=True, verbose_name="Correo Electrónico")
    pass1 = models.CharField(max_length=128, verbose_name="Contraseña")
    pass2 = models.CharField(max_length=128, verbose_name="Confirmar Contraseña")

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'


# Orden del Cliente
class Order(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Usuario =  models.ForeignKey(User, on_delete=models.CASCADE)
    Cantidad = models.IntegerField(default=1) 
    Direccion = models.CharField(max_length=100, default='', blank=True)
    Fecha = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.producto