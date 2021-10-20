from django.shortcuts import render

from .models import Categoria,Plato,Negocio

# Create your views here.
def index(request):
    lstCategorias = Categoria.objects.all()
    lstPlatos = Plato.objects.all()
    objNegocio = Negocio.objects.get(pk=1)

    
    request.session["negocio_telefono"] = objNegocio.telefono
    request.session["negocio_logo"] = objNegocio.imagen.url
    
   
    
    context = {
        'categorias': lstCategorias,
        'platos': lstPlatos,
    }
    return render(request,'menu.html',context)

def plato(request,plato_id):
    objPlato = Plato.objects.get(pk=plato_id)
    context = {
        'plato' : objPlato
    }
    
    return render(request,'plato.html',context)

from .carrito import Cart

def agregarCarrito(request,plato_id):
    objPlato = Plato.objects.get(pk=plato_id)
    cantidad = int(request.POST['cantidad'])
    carrito = Cart(request)
    carrito.add(objPlato,cantidad)
    print(request.session.get("cart"))
    return render(request,'carrito.html')