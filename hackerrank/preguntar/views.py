from django.shortcuts import render
from rest_framework import generics
from .models import Pregunta
from .serializers import PreguntaModelSerializer
from random import randrange

class ListGeneric(generics.ListCreateAPIView):
	ramdom = randrange(len(Pregunta.objects.all()))
	queryset = Pregunta.objects.filter(id=ramdom)
	serializer_class = AlbumTracksSerializer

class DetailGeneric(generics.RetrieveUpdateDestroyAPIView):
	queryset = Pregunta.objects.all()
	serializer_class = AlbumModelSerializer