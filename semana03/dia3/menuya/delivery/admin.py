from django.contrib import admin

# Register your models here.
from .models import Negocio,Categoria,Plato,Cliente

admin.site.register(Negocio)
admin.site.register(Categoria)
admin.site.register(Plato)
admin.site.register(Cliente)