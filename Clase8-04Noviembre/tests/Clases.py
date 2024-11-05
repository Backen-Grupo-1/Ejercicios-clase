#Ejercicio 3
import geopy.distance

class Position:
    def __init__(self, latitud, longitud, altitud):

        if type(latitud) == str or type(longitud) == str or type(altitud) == str: 
            raise TypeError("Wrong type of data type.")
        
        if latitud < -90 or latitud > 90:
            raise ValueError("Latitude out of range!")
        
        self.latitud = latitud

        if longitud < -180 or longitud > 180:
            raise ValueError("Longitude out of range!")
        
        self.longitud = longitud

        if altitud < 0:
            raise ValueError("Altitude cannot be negative!")
        
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
        

# Creo un objeto desde la clase Position forzando el error por escribir una latitud fuera del rango de valores.
# TEST 1
try:
    posicion = Position(-20, -70.64827, -2)
except ValueError as e:
    print(e)

# TEST 2
# try: 
#     concepcion = Position(40, "-20", 1000)
# except Exception as e:
#     print(f"Error: {e}")