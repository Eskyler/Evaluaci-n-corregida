from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from mundial_api.models import Equipo, Jugador
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import EquipoSerializer
from .serializers import JugadorSerializer
from django.contrib.auth import authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def puntoProtegido(request):
    return Response({'status': 'OK'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def mostrarEquipos(request):
    equipos= Equipo.objects.all()
    serializado = EquipoSerializer(equipos, many=True)
    return Response(serializado.data)

# mostrar jugadores de un equipo
@csrf_exempt
@api_view(['GET'])
@permission_classes((AllowAny,))
def mostrarJugadores(request, id):
    try:
        jugadores = Jugador.objects.get(equipo=id)
        serializado = JugadorSerializer(jugadores)
        return Response(serializado.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


# gestionar jugadores
@csrf_exempt
@api_view(['PATCH', 'DELETE', 'POST'])
@permission_classes((IsAuthenticated,))
def gestionarJugador(request, id):
    if request.method == 'PATCH':
        try:
            jugador = Jugador.objects.get(id=id)
            serializador = JugadorSerializer(jugador, data=request.data, partial=True)
            if serializador.is_valid():
                serializador.save()
                return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        try:
            jugador = Jugador.objects.get(id=id)
            jugador.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        try:
            serializador = JugadorSerializer(data=request.data)
            if serializador.is_valid():
                serializador.save()
                return Response(serializador.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
