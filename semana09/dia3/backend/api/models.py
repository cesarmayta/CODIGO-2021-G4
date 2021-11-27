from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    imagen = CloudinaryField('image',default='')

    def __str__(self):
        return self.nombre

from django.contrib.auth.models import User

class Pedido(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.RESTRICT)
    fecha = models.DateField(auto_now=True)
    estado = models.CharField(max_length=1,default='0')

    def __str__(self):
        return str(self.pk)

class PedidoDetalle(models.Model):
    pedido = models.ForeignKey(Pedido,related_name='pedidodetalle',on_delete=models.RESTRICT)
    producto = models.ForeignKey(Producto,related_name='pedidodetalle',on_delete=models.RESTRICT)
    cantidad = models.IntegerField(default=1)
    precio = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return str(self.pk)