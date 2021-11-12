#from django.db import models
from djongo import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200,default='')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200,default='')
    
    def __str__(self):
        return self.nombre