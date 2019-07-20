from django.shortcuts import render
from django.http import HttpResponse

from pendientes.models import Tarea # importamos la clase de model
from random import randint

# Create your views here.

def index(request):
    listita = Tarea.objects.all() #consultamos la BD y guardamos todos
    #los registros de la tabla Tarea
    #como objeto y gurdamos en la listita
    persona = {"nombre":"Marlu",
    "edad": 25,
    "hobbies":["leer","hacer ejercicios","cantar"],
    "lista_tareas":listita
    }

    return render(request, 'inicio.html',persona)

def tarea(request):
    return HttpResponse("hacete la vista gorda")

#crear la vista / 
def tare(request):
    return HttpResponse("cuando la mentira es la verdad")

def inform(request):
    return HttpResponse("la respuesta a todas tus preguntas")
