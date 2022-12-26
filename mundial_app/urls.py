from django.urls import path

from mundial_app import views


urlpatterns = [
    path('equipo/mostrarEquipos/<int:id>', views.mostrarEquipo),
    path('equipo', views.mostrarEquipos)
]