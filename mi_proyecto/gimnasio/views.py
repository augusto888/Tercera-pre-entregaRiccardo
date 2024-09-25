from django.shortcuts import render, redirect
from .models import Cliente, Entrenador, Clase
from .forms import ClienteForm, EntrenadorForm, ClaseForm

def index(request):
    return render(request, 'gimnasio/index.html')

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'gimnasio/crear_cliente.html', {'form': form})

def crear_entrenador(request):
    if request.method == 'POST':
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EntrenadorForm()
    return render(request, 'gimnasio/crear_entrenador.html', {'form': form})

def crear_clase(request):
    if request.method == 'POST':
        form = ClaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClaseForm()
    
    return render(request, 'gimnasio/crear_clase.html', {'form': form})

def listar_clases(request):
    clases = Clase.objects.all()  # Obtiene todas las clases
    return render(request, 'gimnasio/listar_clases.html', {'clases': clases})


def resultados_busqueda(request):
    # Código de la vista aquí
    return render(request, 'resultados_busqueda.html')