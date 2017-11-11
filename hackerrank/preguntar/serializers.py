from rest_framework import serializers
from .models import Pregunta
#from modules.albums.serializers import AlbumModelSerializer

class PreguntaModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pregunta
		fields = ('__all__')