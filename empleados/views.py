from django.shortcuts import render, redirect

# Create your views here.

from .forms import empleadosForm

def add_empleado(request):
    if request.method == 'POST':
        form = empleadosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = empleadosForm()
    return render(request, 'empleados/add_empleado.html', {'form': form})