from django.shortcuts import render
from django.http import HttpResponse

from pendientes.models import Pregunta # importamos la clase de model
from random import randint

# Create your views here.

def index(request):    #esta es la pagina de inicio
    
    return render(request, 'index.html')


#crear la vista / 


def encuesta(request):
    pregunta1= ""
    return render(request, "encuesta.html")

def diccionario(request):
    pregunta1= ""
    return render(request, "diccionario.html")

def pagina1(request): #pagina de registro 
    datos={}
    
    return render(request, "pag1.html")

def pagina2(request):
    datos={}
    data=request.POST.copy()
    nombre=data.get('nombre')
    datos['nombre']=nombre
    email=data.get('email')
    datos['email']=email
    telefono=data.get('telefono')
    datos['telefono']=telefono
    print(datos)
    preguntas=Pregunta.objects.all()
    return render(request, 'pag2.html')
ideas=[]
def pagina3(request):
    
    data=request.POST.copy()
    ideas.append(data.get('idea1'))
    ideas.append(data.get('idea2'))
    ideas.append(data.get('idea3'))
    ideas.append(data.get('idea4'))
    ideas.append(data.get('idea5'))

    return render(request, 'pag3.html',{'ideas':ideas})

ideas_filtro=[] #al sacar de la funcion se convierte en una variable global 
def pagina4(request):
    #logica para filtrar las tres ideas
    
    data=request.POST.copy()
    print(data)
    for i in range(1,6):
        puntuacion=int(data.get('numero'+str(i))) #aqui se reciben las srespuestas en string y se convierte en int y se anhade a la lista 
        if puntuacion >=3: #creamos una variable llamada puntuacion, y vemos si la puntuacion es mayor o igual a tres
#si es asi guardamos la idea en la lista y si no, no se carga
            ideas_filtro.append(ideas[i-1]) #se le carga la ideas ingresadas 
    #cargar
    #GUARDAR EN BASE DE DATOS
    print(ideas_filtro)
    return render(request, 'pag4.html', {'ideas':ideas_filtro}) #aca envia el numero de las ideas seleccionadas
    
def pagina5(request):
    return render(request, 'pag5.html',{'ideas':ideas_filtro})

def pagina6(request):
    return render(request, 'pag6.html',{'ideas':ideas_filtro})

def pagina7(request):
    return render(request, 'pag7.html',{'ideas':ideas_filtro})

def pagina8(request):
    return render(request, 'pag8.html')

def pagina9(request):
    return render(request, 'pag9.html')

def pagina10(request):
    return render(request, 'pag10.html')


def pagina11(request):
    return render(request, 'pag11.html')