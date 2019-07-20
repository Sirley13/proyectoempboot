from django.db import models

# Create your models here.

class Pregunta(models.Model): #la clase tarea hereda metodos de la clase models.Model 
    pregunta = models.CharField(max_length=100) #Campo/columna titulo de tipo "campo de caracteres" de longitud maxima de 100
    nivel = models.IntegerField() #Campo/columna titulo de tipo Texto, los argumentos blank y null son para que el campo sea opcional
    tips = models.TextField(null=True, blank=True) #campo booleano . con todo esto se creo una tabla con base de datos

    def __str__(self):
        return "preguntas:" + self.pregunta 

class Respuestas(models.Model):
    nombre_idea = models.CharField(max_length=100)
    numero_idea = models.IntegerField()
    calificacion =models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=20,null=True, blank=True)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

    def __str__(self):
        return "Respuesta:" + self.nombre_idea 








