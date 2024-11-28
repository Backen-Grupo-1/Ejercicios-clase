from django.views import View
from django.http import JsonResponse
from .models import Libro, Autor, Genero

class LibroListView(View):
    def get(self, request):
        # Recuperar todos los libros
        libros = Libro.objects.values("titulo","genero","autor")
        response_data = {
            "total": libros.count(),
            "libros": list(libros)
        }
        return JsonResponse(response_data, safe=False)