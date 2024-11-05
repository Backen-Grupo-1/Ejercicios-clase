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

Santiago = Position(-33.00,-70.00,24)
print(Santiago.repr_string())
print(Santiago.repr_dicc())