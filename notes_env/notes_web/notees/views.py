from django.shortcuts import render, redirect, get_object_or_404
from .models import Nota
from .forms import NotaForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import time
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponse


def inicio(request):
    return redirect('pagina_inicio')  # Redirige a la página de inicio deseada

def pagina_inicio(request):
    return render(request, 'pagina_inicio.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio_sesion')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lista_notas')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.')  # Añade un mensaje de error
    else:
        form = AuthenticationForm()
    return render(request, 'inicio_sesion.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio_sesion')

@login_required
def lista_notas(request):
    notas = Nota.objects.all()
    return render(request, 'lista_notas.html', {'notas': notas})

@login_required
def crear_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            # Obtener el usuario actual
            creador = request.user
            # Asignar el usuario actual como creador de la nota
            nota = form.save(commit=False)
            nota.creador = request.user  # Asignar el usuario autenticado como creador de la nota
            nota.save()
            return redirect('lista_notas')
    else:
        form = NotaForm()
    return render(request, 'crear_nota.html', {'form': form})

@login_required
def borrar_nota(request, nota_id):
    nota = get_object_or_404(Nota, pk=nota_id)
    nota.delete()
    return redirect('lista_notas')

@login_required
def editar_nota(request, nota_id):
    nota = get_object_or_404(Nota, pk=nota_id)
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('creanota')  # Redirige al espacio de creación después de editar la nota
    else:
        form = NotaForm(instance=nota)
    return render(request, 'crear_nota.html', {'form': form})

@login_required
def detalle_nota(request, nota_id):
    nota = get_object_or_404(Nota, pk=nota_id)
    return render(request, 'detalle_nota.html', {'nota': nota})




