from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import productosForm

def add_producto(request):
    if request.method == 'POST':
        form = productosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = productosForm()
    return render(request, 'productos/add_producto.html', {'form': form})