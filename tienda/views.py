from django.shortcuts import render
from .models import Cliente
# Create your views here.

def index(request):
    return render(request, 'tienda/index.html')

def contacto(request):
    return render(request, 'tienda/contacto.html')

def estadistica(request):
    return render(request, 'tienda/estadistica.html')

def confirmacion(request):
    return render(request, 'tienda/confirmacion.html')

def clientes(request):
    cliente=Cliente.objects.all().values()
    context = {
    'clientes': cliente,
    }
    return render(request, 'tienda/clientes.html', context)
