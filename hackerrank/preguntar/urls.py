from django.conf.urls import url, 
from django.contrib import admin
from .views import ListGenericPregunta, DetailGenericPregunta

urlpatterns = [
url(r'^preguntas/', ListGenericPregunta.asView(), name='listPreguntas'),

]
