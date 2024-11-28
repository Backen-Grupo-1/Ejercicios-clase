from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    autor = models.ManyToManyField('Autor')
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.titulo
    
class Genero(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nombre
    

# python3 manage.py shell

# from biblioteca.models import Autor, Libro, Genero
# from datetime import date

# Crear géneros
# genero_ficcion, created = Genero.objects.get_or_create(nombre='Ficción')
# genero_no_ficcion, created = Genero.objects.get_or_create(nombre='No Ficción')
# genero_ciencia_ficcion, created = Genero.objects.get_or_create(nombre='Ciencia Ficción')

# Crear autores
# autor1, created = Autor.objects.get_or_create(nombre='Gabriel García Márquez', fecha_nacimiento=date(1927, 3, 6))
# autor2, created = Autor.objects.get_or_create(nombre='Isabel Allende', fecha_nacimiento=date(1942, 8, 2))

# Crear libros
# Crear Libro 1: Ficción, escrito por ambos autores
# libro1, created = Libro.objects.get_or_create(titulo='Libro de Ficción Dual', fecha_publicacion=date(2000, 1, 1), genero=genero_ficcion)
# libro1.autor.add(autor1, autor2)

# Crear Libro 2: No Ficción, escrito por un autor (autor1)
# libro2, created = Libro.objects.get_or_create(titulo='Libro de No Ficción', fecha_publicacion=date(2005, 5, 15), genero=genero_no_ficcion)
# libro2.autor.add(autor1)

# Crear Libro 3: Ciencia Ficción, escrito por un autor (autor2)
# libro3, created = Libro.objects.get_or_create(titulo='Libro de Ciencia Ficción', fecha_publicacion=date(2010, 10, 20), genero=genero_ciencia_ficcion)
# libro3.autor.add(autor2)

# Obtener todos los libros escritos por un autor específico
# autor = Autor.objects.get(nombre='Gabriel García Márquez')
# libros_del_autor = Libro.objects.filter(autor=autor)
# print(f"Libros escritos por {autor.nombre}:")
# for libro in libros_del_autor:
#     print(f"- {libro.titulo}")

# Contar Cuántos Libros Pertenecen al Género Ficción
# genero_ficcion = Genero.objects.get(nombre='Ficción')
# cantidad_libros_ficcion = Libro.objects.filter(genero=genero_ficcion).count()
# print(f"Número de libros en el género {genero_ficcion.nombre}: {cantidad_libros_ficcion}")

# Obtener el Título del Primer Libro Ordenado por Fecha de Publicación
# primer_libro = Libro.objects.order_by('fecha_publicacion').first()
# if primer_libro:
#     print(f"El primer libro publicado es: {primer_libro.titulo}")
# else:
#     print("No hay libros en la base de datos.")
