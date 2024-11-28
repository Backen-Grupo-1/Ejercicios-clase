from django.views import View
from django.http import JsonResponse
from .models import Libro, Autor, Genero

class LibroListView(View):
    def get(self, request):
        libros = Libro.objects.all()
        
        libros_data = []
        for libro in libros:
            autores = [autor.nombre for autor in libro.autor.all()]
            genero = libro.genero.nombre if libro.genero else "Sin género"
            libros_data.append({
                "titulo": libro.titulo,
                "genero": genero,
                "autores": autores
            })
        
        response_data = {
            "total": libros.count(),
            "libros": libros_data
        }
        
        return JsonResponse(response_data)