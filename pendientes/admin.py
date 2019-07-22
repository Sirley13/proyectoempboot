from django.contrib import admin
from .models import Pregunta, Respuestas #importamos el modelo

# Register your models here.

admin.site.register(Pregunta) # lo registramos
admin.site.register(Respuestas)