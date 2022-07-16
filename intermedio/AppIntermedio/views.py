from django.shortcuts import render
from .models import Libro

# Create your views here.



def libros(request):
    libros = Libro.objects.all()
    print(libros)
    return render(request,"libros/index.html",{'libros': libros})

def inicio(request):
    return render(request,"AppIntermedio/inicio.html")

def crear(request):
    return render(request,"libros/crear.html") 

def editar(request):
    return render(request,"libros/editar.html") 