from django.urls import path 
from aplicacion_final. views import *


urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("formulario_contacto/", formulario_contacto, name="formulario"),
    path("servicios/", servicios, name="servicios"),
    path("sugerencias/", sugerencias_mejora, name="sugerencias"),
    path("formulario_contacto/buscar/", buscar_contacto, name="buscar_contacto" ),
    path("formulario_contacto/buscar/resultado/", resultados_busqueda_contacto, name="resultado_buscar_contacto" ),
    path("formulario_email/", formulario_email, name="formulario_email" ),
]