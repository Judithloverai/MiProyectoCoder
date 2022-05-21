import django


from django import forms

class ConsultaFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    consulta = forms.CharField()

class ProfesionalesFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    cargo = forms.CharField()


  
