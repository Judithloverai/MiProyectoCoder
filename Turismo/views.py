from django.http import HttpResponse
from django.shortcuts import render
from Turismo.models import Destino

def destino(self):

    destino1=Destino(nomnre="Tokio", unbicacion="Japón")

    destino.sabve()

    documento = f"El destino de viaje es {destino.nombre} y su ubicación es {destino.ubicacion}"

    return HttpResponse(documento)