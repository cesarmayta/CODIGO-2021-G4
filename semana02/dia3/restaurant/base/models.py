from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
class Plato(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,null=True)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    
    def __str__(self):
        return self.nombre