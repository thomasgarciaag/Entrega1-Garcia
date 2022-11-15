from django.shortcuts import render
from aplicacion_final import *
from django.http import HttpResponse
from aplicacion_final.models import *
from aplicacion_final.forms import *

# Create your views here.

def inicio(request):
    return render(request, "aplicacion_final/base.html")
  

def formulario_contacto(request):

    if request.method == "POST":
        formulario = contacto_formulario(request.POST) 

        if formulario.is_valid():
            data = formulario.cleaned_data

            Contacto = contacto(nombre=data["nombre"], telefono=data["telefono"]) 
            Contacto.save()            

    
    formulario  = contacto_formulario()
         
    contexto = {"formulario": formulario}

    return render(request, "aplicacion_final/formulario_contacto.html", contexto)       



def sugerencias_mejora(request):

    if request.method == "POST":
        formulario = sugerencia_formulario(request.POST) 

        if formulario.is_valid():
            data = formulario.cleaned_data

            Sugerencia = sugerencia(nombre=data["nombre"], sugerencia=data["sugerencia"]) 
            Sugerencia.save()
    

    formulario  = sugerencia_formulario()

         
    contexto = {"formulario": formulario}

    return render(request, "aplicacion_final/sugerencias.html", contexto)  



def formulario_email(request):

    if request.method == "POST":
        formulario = contacto_email(request.POST) 

        if formulario.is_valid():
            data = formulario.cleaned_data

            Contacto = email(nombre=data["nombre"], email=data["email"]) 
            Contacto.save()
    

    formulario  = contacto_email()

         
    contexto = {"formulario": formulario}

    return render(request, "aplicacion_final/formulario_email.html", contexto)  







def buscar_contacto(request):
    return render (request, "aplicacion_final/busqueda_contacto.html")

def resultados_busqueda_contacto(request):

    nombre_contacto = request.GET["nombre_buscado"]

    Contactos = contacto.objects.filter(nombre__icontains=nombre_contacto)


    return render (request, "aplicacion_final/resultados_busqueda_contacto.html", {"Contactos":Contactos})
    








def servicios(request):
    return render(request, "aplicacion_final/servicios.html")   