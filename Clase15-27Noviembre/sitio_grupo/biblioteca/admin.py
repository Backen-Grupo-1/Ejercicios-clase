from django.contrib import admin

# Register your models here.
from .models import Autor, Libro, Genero
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Genero)
