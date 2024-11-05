#Ejercicio 3
import geopy.distance

class Position:
    def __init__(self, latitud, longitud, altitud):
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud
    def repr_string(self):
        return f"{self.latitud}, {self.longitud}, {self.altitud}"
    def repr_dicc(self):
        dic = {"Latitud": self.latitud, "Longitud": self.longitud, "Altitud": self.altitud}
        return dic

class Waypoint(Position):
    def __init__(self, nombre):
        self.nombre = nombre

class Trackpoint(Position):
    def __init__(self, fecha_registro):
        self.fecha_registro = fecha_registro

class Distance:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    def km(self):
        return geopy.distance.geodesic(self.source, self.destination).km
        

Santiago = (-33.45694,-70.64827)
Vina = (-33.02457,-71.55183)
print(Distance(Santiago,Vina).km())