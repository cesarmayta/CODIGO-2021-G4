class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        totalCart = self.session.get("totalCart")
        if not cart:
            cart = self.session["cart"] = {}
            totalCart = self.session["totalCart"] = 0
        self.cart = cart
        self.totalCart = totalCart
        
    def add(self,plato,qty):
        if str(plato.id) not in self.cart.keys():
            self.cart[plato.id] = {
                "plato_id": plato.id,
                "nombre" : plato.nombre,
                "cantidad" : qty,
                "precio": str(plato.precio),
                "imagen" : plato.imagen.url,
                "total" : str(qty * plato.precio)
                }
        else:
            for key,value in self.cart.items():
                if key == str(plato.id):
                    value["cantidad"] = str(int(value["cantidad"]) + qty)
                    value["total"] = str(float(value["cantidad"]) * float(value["precio"]))
                    break
        
        self.save()
        
    def save(self):
        self.session["cart"] = self.cart
        
        total = 0
        for key,value in self.cart.items():
            total = total + (float(value["cantidad"]) * float(value["precio"]))
                                               
        self.session["totalCart"] = total
        
        self.session.modified = True
        
    def remove(self,plato):
        plato_id = str(plato.id)
        if plato_id in self.cart:
            del self.cart[plato_id]
            self.save()
            
    def clear(self):
        self.session["cart"] = {}
        self.session["totalCart"] = 0