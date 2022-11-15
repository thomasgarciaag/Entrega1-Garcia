from django import forms

class sugerencia_formulario(forms.Form):

    nombre = forms.CharField()
    sugerencia = forms.CharField()

    
class contacto_formulario(forms.Form):

    nombre = forms.CharField()
    telefono = forms.IntegerField()


class contacto_email(forms.Form):

    nombre = forms.CharField()
    email = forms.EmailField()