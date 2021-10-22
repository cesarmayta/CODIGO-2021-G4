from django.urls import path

from . import views

app_name = 'delivery'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:plato_id>',views.plato,name='plato'),
    path('agregarCarrito/<int:plato_id>',views.agregarCarrito,name='agregarCarrito'),
    path('carrito',views.mostrarCarrito,name='carrito'),
    path('eliminarCarrito/<int:plato_id>',views.eliminarPlatoCarrito,name='eliminarCarrito'),
    path('limpiarCarrito',views.limpiarCarrito,name='limpiarCarrito'),
    path('login',views.loginUsuario,name='login'),
    path('registro',views.registroCliente,name='registro'),
    path('pedido',views.registrarPedido,name='pedido'),
    path('gracias',views.gracias,name='gracias'),
    path('confirmarPedido',views.confirmarPedido,name='confirmarPedido')
]