from django.shortcuts import render
from productos.models import productos

# Create your views here.

def home(request):
    productos = None
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        productos = productos.objects.filter(nombre__icontains=nombre)
    return render(request, 'home.html', {'productos': productos})