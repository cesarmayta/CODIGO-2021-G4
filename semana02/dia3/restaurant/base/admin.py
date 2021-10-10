from django.contrib import admin

# Register your models here.
from .models import Plato,Categoria

admin.site.register(Plato)
admin.site.register(Categoria)