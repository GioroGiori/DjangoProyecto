from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('colaborador', views.colaborador, name="colaborador"),
    path('agregarPersonaje', views.personajeAdd, name="personajeAdd"),
    path('personaje_edit/<str:pk>', views.personaje_edit, name="personaje_edit"),
    path('personaje_del/<str:pk>', views.personaje_del, name="personaje_edit")
]
