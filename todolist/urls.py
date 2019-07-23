"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pendientes import views
#from es desde tal carpeta traer a tal cosa, import es importar 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), #Creamos la ruta raiz '' y la enlazamos con nuestra vista index del archivo views.py
    path("pag1", views.pagina1),
    path("pag2", views.pagina2),
    path("pag3", views.pagina3),
    path("pag4", views.pagina4),
    path("pag5", views.pagina5),
    path("pag6", views.pagina6),
    path("pag7", views.pagina7),
    path("pag8", views.pagina8),
    path("pag9", views.pagina9),
    path("pag10", views.pagina10),
    path("pag11", views.pagina11),
    path("encuesta", views.encuesta),
    path("diccionario", views.diccionario),


    # path("tareas", views.tarea),
    #path("inform", views.inform),
    #path("inicio", views.index) #la palabra adherida debe coincidir con la palabra que vamos a poner en la pagina con la barra 
]