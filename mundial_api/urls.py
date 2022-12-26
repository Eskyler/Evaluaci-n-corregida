from pathlib import Path
from django.urls import path

from mundial_api import views

urlpatterns = [
    path('equipos/', views.mostrarEquipos),
    path('test-protegido/', views.puntoProtegido),
    path('jugador/<int:id>', views.mostrarJugadores),
    path('equipos/', views.mostrarEquipos),
    path('jugador/editar/<int:id>', views.gestionarJugador)
]