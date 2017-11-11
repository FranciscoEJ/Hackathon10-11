from django.db import models

# Create your models here.

class Pregunta(models.Model):
	
	id = models.AutoField(primary_key=True)
	pregunta = models.CharField(max_length=100)
	respuesta = models.CharField(max_length=100)
	
