import django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class RegistroFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
