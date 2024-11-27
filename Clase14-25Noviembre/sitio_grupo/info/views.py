from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

def inicio(request):
    return HttpResponse('Bienvenidos al sitio web del grupo 1')

def proyecto(request, proyecto = None):
    if not proyecto:
        return HttpResponseBadRequest('Debe ingresar nombre proyecto')
    return HttpResponse(f'Detalles del proyecto: {proyecto.capitalize()}')
    
def proyecto_v2(request, nombre, descripcion, estado):
    context = {
    'nombre': nombre.capitalize(),
    'descripcion': descripcion.capitalize(),
    'estado': estado.capitalize()
    }
    return render(request, 'proyecto.html', context)