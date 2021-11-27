from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Categoria,Producto,Pedido,PedidoDetalle
from .serializers import CategoriaSerializer,ProductoSerializer,PedidoSerializer

@api_view(['GET'])
def categoria(request):
    lstCategoria = Categoria.objects.all()
    serCategoria = CategoriaSerializer(lstCategoria,many=True)
    return Response(serCategoria.data)

@api_view(['GET'])
def producto(request):
    lstProducto = Producto.objects.all()
    serProducto = ProductoSerializer(lstProducto,many=True)
    return Response(serProducto.data)

@api_view(['POST','GET'])
def pedido(request):
    if request.method == 'POST':
        serPedido = PedidoSerializer(data=request.data)
        if serPedido.is_valid():
            serPedido.save()
            return Response(serPedido.data)
        else:
            return Response(serPedido.errors)
    elif request.method == 'GET':
        lstPedido = Pedido.objects.all()
        serPedido = ProductoSerializer(lstPedido,many=True)
        return Response(serPedido.data)
    
    