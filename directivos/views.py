from django.shortcuts import render, redirect

# Create your views here.

from .forms import directivosForm

def add_directivo(request):
    if request.method == "POST":
        form = directivosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = directivosForm()
    return render(request, 'directivos/add_directivo.html', {'form': form})