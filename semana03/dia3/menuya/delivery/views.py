from django.shortcuts import render

from .models import Categoria,Plato

# Create your views here.
def index(request):
    lstCategorias = Categoria.objects.all()
    lstPlatos = Plato.objects.all()
    
    context = {
        'categorias': lstCategorias,
        'platos': lstPlatos
    }
    return render(request,'menu.html',context)

def plato(request,plato_id):
    objPlato = Plato.objects.get(pk=plato_id)
    context = {
        'plato' : objPlato
    }
    
    return render(request,'plato.html',context)