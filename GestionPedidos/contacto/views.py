from django.shortcuts import render, HttpResponse, redirect

from .forms import FormularioContacto

from django.core.mail import EmailMessage

from .models import Contacto

# Create your views here.
def contacto(request):
    #Se instancia el formulario creado en forms 
    # para luego pasarlo como parametro a la plantilla
    Formulario_Contacto = FormularioContacto()

    #Una vez instanciado el formulario se debe preguntar
    #si se utilizo el metodo POST
    if request.method == 'POST':
        Formulario_Contacto=FormularioContacto(data=request.POST)
        #Si el formulario es valido(se lleno bien)
        if Formulario_Contacto.is_valid():
            #Guarda cada valor en una variable lo que hay en cada campo
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde mi primer web django")

            obj = Contacto()
            obj.nombre = nombre
            obj.email = email
            obj.contenido = contenido
            obj.save()

            return redirect("/contacto/")

    return render(request, 'contacto/contacto.html', {'miFormulario':Formulario_Contacto})

