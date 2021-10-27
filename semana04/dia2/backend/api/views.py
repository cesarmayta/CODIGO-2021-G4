from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Producto
from .serializers import ProductoSerializer

# Create your views here.
@api_view(['GET'])
def productos(request):
    lstProductos = Producto.objects.all()
    serProductos = ProductoSerializer(lstProductos,many=True)
    return Response(serProductos.data)
