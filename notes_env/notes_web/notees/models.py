# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Nota(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo