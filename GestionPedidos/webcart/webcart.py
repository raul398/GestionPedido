#Creamos la clase de webcart que maneja la sesion

class webcart:
    #Constructor que iniciara las tareas mas importantes
    def __init__(self, request):
        #Almacenar la peticion actual para utilizarla mas adelante
        self.request = request #almacena la peticion
        self.session = request.session #inicia la session
        #contruir un carro de la compra que el usuario de turno usara
        webcart = self.session.get('webcart')
        #si no hay carro debe lo crea sino respeta el que estaba en session
        if not webcart:
            self.webcart = self.session['webcart'] = {}
        else:
            self.webcart = webcart

    #debe agregar productos
    def add(self, producto):
        #validar si el producto ya esta en el carro
        if(str(producto.id) not in self.webcart.keys()):
            #si no existe crea la kay del producto en el carro
            self.webcart[producto.id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'precio': str(producto.precio),
                'cantidad':1,
                'imagen': producto.imagen.url
            }
        elif str(producto.id) in self.webcart.keys():
            #si ya existe ponemos la opcion de agregar cantidad
            self.webcart[str(producto.id)]['cantidad'] += 1

        #Hay que actualizar el carro dentro de la session
        self.save_webcart()

    
    #este metodo actualiza los valores dentro de la session
    def save_webcart(self):
        self.session['webcart'] = self.webcart
        self.session.modified = True

    #elimina un articulo por comppleto del carro
    def delete(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.webcart:
            del self.webcart[producto.id]
            self.save_webcart()

    #resta cantidades de un producto existente en el carro
    def quit_count(self, producto):
        if str(producto.id) in self.webcart.keys():
            #si ya existe ponemos la opcion de restar cantidad
            self.webcart[str(producto.id)]['cantidad'] -= 1
        if self.webcart[str(producto.id)]['cantidad'] < 1:
            #si al restar el producto queda en cero se elimina del carro
            self.delete(producto)
        self.save_webcart()

    def clear_webcart(self):
        #este metodo vacia el carro
        self.session['webcart'] = {}
        self.session.modified = True
