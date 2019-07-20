from django.shortcuts import render
from django.http import HttpResponse

from pendientes.models import Pregunta # importamos la clase de model
from random import randint

# Create your views here.

def index(request):
    listita = Pregunta.objects.all() #consultamos la BD y guardamos todos
    #los registros de la tabla Tarea
    #como objeto y gurdamos en la listita
    persona = {"nombre":"Marlu",
    "edad": 25,
    "hobbies":["leer","hacer ejercicios","cantar"],
    "lista_tareas":listita
    }

    return render(request, 'index.html',persona)

def test(request):
    return HttpResponse("hacete la vista gorda")

#crear la vista / 
def encuesta(request):
    pregunta1= ""
    return render(request, "encuesta.html")

def inform(request):
    return HttpResponse("la respuesta a todas tus preguntas")
