from django.shortcuts import render, redirect
from .models import Juguetes, Marcas
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def buscar_juguetes(request):
    query = request.GET.get('q')
    juguete = Juguetes.objects.filter(
        Q(modelo__icontains=query) |
        Q(descripcion__icontains=query) |
        Q(precio__icontains=query) |
        Q(marca__nombre__contains=query) |
        Q(disponibilidad__icontains=query)
    )
    return render(request, 'InicioJuguetes.html', {'juguete': juguete})

def inicioDef(request):
    juguete = Juguetes.objects.all()
    return render(request, 'InicioJuguetes.html', {'juguete': juguete})

def crearJugueteDef(request):
    marca = Marcas.objects.all()
    return render(request, 'GestionarJuguetes.html', {'marca': marca})

def registrarJugueteDef(request):
    id = request.POST['txtId']
    modelo = request.POST['txtModelo']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    marca_id = request.POST['txtMarca']
    marca = Marcas.objects.get(id=marca_id)
    disponibilidad = request.POST['txtDisponibilidad']

    try:
        juguete = Juguetes.objects.create(
            id=id, modelo=modelo,
            descripcion=descripcion,
            precio=precio,
            disponibilidad=disponibilidad,
            marca=marca)
        messages.success(request, 'juguete Añadido Correctamente.')
        return render(request, 'GestionarJuguetes.html', {'mensaje_tipo': 'success', 'mensaje_texto': 'Juguete Añadido Correctamente.'})

    except:
        messages.error(request, 'Ocurrió un error durante el registro. Por favor revise, inténtelo de nuevo.')
        return render(request, 'GestionarJuguetes.html', {'mensaje_tipo': 'error', 'mensaje_texto': 'Ocurrió un error durante el registro. Por favor revise, inténtelo de nuevo.'})

def editarJugueteDef(request, id):
    juguete = Juguetes.objects.get(id=id)
    marca = Marcas.objects.all()
    return render(request, 'EditarJuguetes.html', {'juguete': juguete, 'marca': marca})

def edicionJugueteDef(request):
    id = request.POST['txtId']
    modelo = request.POST['txtModelo']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    disponibilidad = request.POST['txtDisponibilidad']

    juguete = Juguetes.objects.get(id=id)
    juguete.modelo = modelo
    juguete.descripcion = descripcion
    juguete.precio = precio
    juguete.disponibilidad = disponibilidad
    juguete.save()


    return redirect('inicio')

def borraJugueteDef(request, id):
    juguete = Juguetes.objects.get(id=id)
    juguete.delete()
    return redirect('inicio')