from django.contrib import admin

# Register your models here.
from .models import Negocio,Categoria,Plato,Cliente,FormaPago,Pedido,PedidoDetalle

admin.site.register(Negocio)
admin.site.register(Categoria)
admin.site.register(Plato)
admin.site.register(Cliente)
admin.site.register(FormaPago)
admin.site.register(Pedido)
admin.site.register(PedidoDetalle)