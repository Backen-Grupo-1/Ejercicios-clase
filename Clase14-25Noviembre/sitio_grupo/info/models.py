from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    fecha_inicio = models.DateField()
    def __str__(self):
        return self.name