#Ejercicio 1
class Position:
    def __init__(self, latitud, longitud, altitud):
        self.latitud = latitud
        self.longitud = longitud
        self.latitud = altitud

class Waypoint(Position):
    def __init__(self, nombre):
        self.nombre = nombre

class Trackpoint(Position):
    def __init__(self, fecha_registro):
        self.fecha_registro = fecha_registro

P = Position(-33.00,34.95,24)
print(P)