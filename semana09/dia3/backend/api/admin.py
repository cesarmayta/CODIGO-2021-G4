from django.contrib import admin

# Register your models here.
from .models import Categoria,Producto,Pedido,PedidoDetalle

admin.site.register(Categoria)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('pk','nombre','categoria','precio')
    search_fields = ['nombre']

admin.site.register(Pedido)
admin.site.register(PedidoDetalle)