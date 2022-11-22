from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index', views.index, name="index"),
    path('colaborador', views.colaborador, name="colaborador"),
    path('crud_personajes', views.crud_personajes, name="crud_personajes"),
    path('agregarPersonaje', views.agregarPersonaje, name="agregarPersonaje"),
    path('personaje_edit/<str:pk>', views.personaje_edit, name="personaje_edit"),
    path('personaje_del/<str:pk>', views.personaje_del, name="personaje_del"),
    path('login', views.login, name="login"),
    path('loginData', views.loginData, name="loginData"),
    path('quienesSomos', views.quienesSomos, name="quienesSomos"),
    path('listarPersonaje', views.listarPersonaje, name="listarPersonaje"),
    path('personajes', views.personajes, name="personajes"),
    path('administracion', views.administracion, name="administracion")
]
