from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from mundial_api.serializers import EquipoSerializer, JugadorSerializer
from mundial_api.models import Jugador, Equipo




def mostrarEquipos(request):
    datos = {
        "equipo": [
            {"nombre": "Real Madrid", "año_creacion": "1902", "Campeon": True, "imagen": "img/realM.png"},
            {"nombre": "Barcelona", "año_creacion":"1899", "Campeon": True, "imagen": "img/barcaCamp.png"},
        ]
    }
    return render(request, 'equipo/equipo.html', datos)



#def mostrarEquipo(request):
#    return render(request, 'equipo/equipo.html')

@csrf_exempt
@permission_classes((AllowAny,))
def mostrarEquipo(request,id):
    try:
        equipo= Equipo.objects.filter(id=id).first
        data={'equipo' : equipo}
        return render(request,"equipo/equipos.html",data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


