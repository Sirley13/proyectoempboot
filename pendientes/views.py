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


#crear la vista / 


def encuesta(request):
    pregunta1= ""
    return render(request, "encuesta.html")

def inform(request):
    return HttpResponse("la respuesta a todas tus preguntas")


def pagina2(request):
    return render(request, 'pag2.html')


def pagina3(request):
    return render(request, 'pag3.html')

def pagina4(request):
    return render(request, 'pag4.html')
