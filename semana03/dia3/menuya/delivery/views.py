from django.shortcuts import render,redirect

from .models import Categoria,Plato,Negocio,Cliente

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

def mostrarCarrito(request):
    return render(request,'carrito.html')

def eliminarPlatoCarrito(request,plato_id):
    objPlato = Plato.objects.get(pk=plato_id)
    carrito = Cart(request)
    carrito.remove(objPlato)
    return redirect('/delivery/carrito')

def limpiarCarrito(request):
    carrito = Cart(request)
    carrito.clear()
    return redirect('/delivery/carrito')

from django.contrib.auth import authenticate,login,logout

def loginUsuario(request):
    
    if request.method == 'POST':
        dataUsuario = request.POST['usuario']
        dataClave = request.POST['clave']
        
        print(dataUsuario)
        
        loginUsuario  = authenticate(request,username=dataUsuario,password=dataClave)
        if loginUsuario is not None:
            login(request,loginUsuario)
            return redirect('/delivery/carrito')
        
        
    
    return render(request,'login.html')

from django.contrib.auth.models import User

def registroCliente(request):
    
    if request.method == 'POST':
        #registrar un nuevo cliente
        usuario = request.POST['usuario']
        clave = request.POST['password']
        
        nuevoUsuario = User.objects.create_user(username=usuario,password=clave)
        
        nuevoUsuario.first_name = request.POST['nombre']
        nuevoUsuario.last_name = request.POST['apellido']
        nuevoUsuario.email = request.POST['email']
        
        nuevoUsuario.save()
        
        nuevoCliente = Cliente(usuario=nuevoUsuario)
        nuevoCliente.telefono = request.POST['telefono']
        nuevoCliente.save()
        
        return redirect('/delivery/login')
    
    return render(request,'registro.html')
    