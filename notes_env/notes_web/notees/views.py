from django.shortcuts import render, redirect
from .models import Nota
from .forms import NotaForm


# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola! estás en el index de la agenda.")

def lista_notas(request):
    notas = Nota.objects.all()
    print("Esta es la lista de notas")
    return render(request, 'lista_notas.html', {'notas': notas})

def crear_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')  # Redirige a la lista de notas después de crear una nueva nota
    else:
        form = NotaForm()
    return render(request, 'crear_nota.html', {'form': form})
