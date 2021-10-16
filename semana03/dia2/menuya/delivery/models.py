from django.db import models

# Create your models here.
class Negocio(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='negocio',blank=True,null=True)
    precioEnvio = models.DecimalField(max_digits=9,decimal_places=2)
    calificacion = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
class Plato(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='plato',blank=True,null=True)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    negocio = models.ForeignKey(Negocio,on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.nombre
    
    