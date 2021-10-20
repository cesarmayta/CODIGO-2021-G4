from django.db import models

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
    
    