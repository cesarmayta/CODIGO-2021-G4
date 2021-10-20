from django.urls import path

from . import views

app_name = 'delivery'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:plato_id>',views.plato,name='plato'),
    path('agregarCarrito/<int:plato_id>',views.agregarCarrito,name='agregarCarrito')
]