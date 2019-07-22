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
datos={}
def pagina3(request):
<<<<<<< HEAD
<<<<<<< HEAD
    nombre = request.POST.get("nombre")
    print(nombre)
    mail = request.POST.get("mail")
    print(mail)
    return render(request, 'pag4.html')
=======
=======
    data=request.POST.copy()
    nombre=data.get('nombre')
    datos['nombre']=nombre
    email=data.get('email')
    datos['email']=email
    telefono=data.get('telefono')
    datos['telefono']=telefono
    preguntas=Pregunta.objects.all()
>>>>>>> b7fbbd92d4e3af20836b5172bd4eb56531d7fe4f
    return render(request, 'pag3.html')
>>>>>>> 97cde4e42a31a8c32322b18a1f61f5856f36e5f8

def pagina4(request):
    ideas=[]
    data=request.POST.copy()
    ideas.append(data.get('idea1'))
    ideas.append(data.get('idea2'))
    ideas.append(data.get('idea3'))
    ideas.append(data.get('idea4'))
    ideas.append(data.get('idea5'))
    print(ideas)
    return render(request, 'pag4.html', {'ideas':ideas})
    
def pagina5(request):
    return render(request, 'pag5.html')