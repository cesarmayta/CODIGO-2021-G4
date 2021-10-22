from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Negocio(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='negocios',blank=True,null=True)
    telefono = models.CharField(max_length=50,default='')
    precioEnvio = models.DecimalField(max_digits=9,decimal_places=2)
    calificacion = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='categorias',blank=True,null=True)
    
    def __str__(self):
        return self.nombre
    
class Plato(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='platos',blank=True,null=True)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    negocio = models.ForeignKey(Negocio,on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.nombre
    
class FormaPago(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.RESTRICT)
    telefono = models.CharField(max_length=20)
    
    def __str__(self):
        return self.telefono
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.RESTRICT)
    direccion = models.CharField(max_length=200)
    fechaHora = models.DateTimeField(auto_now=True)
    formaPago = models.ForeignKey(FormaPago,on_delete=models.RESTRICT)
    totalPagar = models.DecimalField(max_digits=9,decimal_places=2)
    montoPago = models.DecimalField(max_digits=20,decimal_places=2)
    
    def __str__(self):
        return str(self.fechaHora)
    
class PedidoDetalle(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete=models.RESTRICT)
    plato = models.ForeignKey(Plato,on_delete=models.RESTRICT)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    cantidad = models.IntegerField(default=1)
    
    def __str__(self):
        return self.plato.nombre
    
    
    



    

    
    