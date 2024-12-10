from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):
    """
    Habitaciones del mejor hotel.
    
    Variables:
    - name (str): Tipo de habitación.
    - description (str): Descripción.
    - price_per_night (int): Valor de la habitación en dolares.
    - is_available (bool): Si esta disponible o no (True/False).
    """
    
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    price_per_night = models.IntegerField()
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.name} {self.price_per_night}'
    
class Reservation(models.Model):
    """
    Usuarios.
    
    Variables:
    - user (str): Usarios.
    - room (str): Habitación.
    - start_date (date): Desde cuando reserva.
    - end_date (date): Hasta cuenado reserva.
    """
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return f'{self.user} {self.room} {self.start_date} {self.end_date}'
    
   