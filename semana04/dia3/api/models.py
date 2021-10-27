from django.db import models

from cloudinary.models import CloudinaryField


# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    #imagen = models.ImageField(upload_to='productos')
    imagen = CloudinaryField('image',default='')
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    
    def __str__(self):
        return self.nombre