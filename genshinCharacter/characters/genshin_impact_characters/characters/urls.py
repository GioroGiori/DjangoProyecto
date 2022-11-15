from django.contrib import admin
from django.urls import path

from . import views

urlpatterns=[
    path('login', views.login, name="login"),
    path('loginData', views.loginData, name="loginData"),
    path('index', views.index, name="index"),
    path('error', views.error, name="error"),
    path('characterAdd', views.characterAdd, name="characterAdd"),
    path('characters_del/<str:pk>', views.characters_del, name='characters_del'),
    path('characters_edit/<str:pk>', views.characters_edit, name='characters_edit'),
]
