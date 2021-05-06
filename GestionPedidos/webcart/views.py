from django.shortcuts import render

from .webcart import WebCart
 
from tienda.models import Producto

from django.shortcuts import redirect

# Create your views here.


def add(request, producto_id):
    #crear el carro
    webcart = WebCart(request)
    #obtener el producto que vamos a mete al carro
    producto = Producto.objects.get(id=producto_id)
    #ahora agregamos este producto al carro
    webcart.add(producto=producto)
    #volvemos a la tienda
    return redirect('tienda')

def delete(request, producto_id):
    #crear el carro
    webcart = WebCart(request)
    #obtener el producto que vamos a mete al carro
    producto = Producto.objects.get(id=producto_id)
    #ahora eliminamos este producto al carro
    webcart.delete(producto=producto)
    #volvemos a la tienda
    return redirect('tienda')

def quit_count(request, producto_id):
    #crear el carro
    webcart = WebCart(request)
    #obtener el producto que vamos a mete al carro
    producto = Producto.objects.get(id=producto_id)
    #ahora restamos este producto al carro
    webcart.quit_count(producto=producto)
    #volvemos a la tienda
    return redirect('tienda')

def clear_webcart(request, producto_id):
    #crear el carro
    webcart = WebCart(request)
    #limpiar el carro
    webcart.clear_webcart()
    #volvemos a la tienda
    return redirect('tienda')
