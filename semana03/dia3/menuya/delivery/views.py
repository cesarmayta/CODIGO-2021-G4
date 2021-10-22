from django.shortcuts import render,redirect

from .models import Categoria,Plato,Negocio,Cliente,FormaPago,Pedido,PedidoDetalle

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
    context = {}
    
    if request.method == 'POST':
        dataUsuario = request.POST['usuario']
        dataClave = request.POST['clave']
        
        print(dataUsuario)
        
        
        
        loginUsuario  = authenticate(request,username=dataUsuario,password=dataClave)
        if loginUsuario is not None:
            login(request,loginUsuario)
            return redirect('/delivery/pedido')
        else:
            context = {
                'error':'datos incorrectos'
            }
        
    
    return render(request,'login.html',context)

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

def registrarPedido(request):
   
    if request.user.id is not None:
        usuarioPedido = User.objects.get(pk=request.user.id)
        clientePedido = Cliente.objects.get(usuario=usuarioPedido)
        lstFormasPago = FormaPago.objects.all()
        context = {
            'nombres':request.user.first_name,
            'apellidos':request.user.last_name,
            'telefono':clientePedido.telefono,
            'email':request.user.email,
            'formaspago': lstFormasPago
            
        }
    else:
        return redirect('/delivery/login')
    
    
    return render(request,'pedido.html',context)

def confirmarPedido(request):
    #REGISTRO PEDIDO EN BASE DE DATOS
    print("ENVIANDO PEDIDO.....")
    usuarioPedido = User.objects.get(pk=request.user.id)
    clientePedido = Cliente.objects.get(usuario=usuarioPedido)
    dataFormaPagoId = request.POST['chkFormaPago']
    dataDireccion = request.POST['direccion']
            
    dataFormaPago = FormaPago.objects.get(pk=dataFormaPagoId)
            
    nuevoPedido = Pedido()
    nuevoPedido.cliente = clientePedido
    nuevoPedido.direccion = dataDireccion
    nuevoPedido.formaPago = dataFormaPago
    nuevoPedido.totalPagar = float(request.session.get("totalCart"))
    nuevoPedido.montoPago = 0
    nuevoPedido.save()
    
    #registramos detalle de pedido
    carritoPedido = request.session.get("cart")
    for key,value in carritoPedido.items():
        nuevoDetalle = PedidoDetalle()
        nuevoDetalle.pedido = nuevoPedido
        nuevoDetalle.cantidad = int(value["cantidad"])
        nuevoDetalle.precio = float(value["precio"])
        
        detallePlato = Plato.objects.get(pk=value["plato_id"])
        
        nuevoDetalle.plato = detallePlato
        nuevoDetalle.save()
    
    carrito = Cart(request)
    carrito.clear()
    return render(request,'gracias.html')
    
def gracias(request):
    return render(request,'gracias.html')