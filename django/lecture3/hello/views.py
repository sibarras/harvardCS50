from django.shortcuts import render
#New
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# New
def index(request):
    return render(request, "hello/index.html")

def samuel(request):
    return HttpResponse("Hello, Samuel!")

def luz(request):
    return HttpResponse("Hello, Luz!")

# Render carga una pagina html en la ruta, y
# el parametro name puede ser pasado como un diccionario
# en el que el key es usado por el html 
def greet(request, name:str):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
