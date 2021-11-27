from django.urls import path

from . import views

urlpatterns = [
    path('categoria',views.categoria),
    path('producto',views.producto),
    path('pedido',views.pedido)
]