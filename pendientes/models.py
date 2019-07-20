from django.db import models

# Create your models here.

class Tarea(models.Model): #la clase tarea hereda metodos de la clase models.Model 
    titulo = models.CharField(max_length=100) #Campo/columna titulo de tipo "campo de caracteres" de longitud maxima de 100
    descripcion = models.TextField(null=True, blank=True) #Campo/columna titulo de tipo Texto, los argumentos blank y null son para que el campo sea opcional
    estado = models.BooleanField(default=False) #campo booleano . con todo esto se creo una tabla con base de datos

    def __str__(self):
        return "tarea:" + self.titulo +" "+ str(self.estado)


