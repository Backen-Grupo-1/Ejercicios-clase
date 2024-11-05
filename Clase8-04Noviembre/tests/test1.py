from Clases import Position, Waypoint, Trackpoint, Distance

santiago = Position(-33.45694, -70.64827, 520)
concepcion = Position(-36.82699, -73.04977, 12)

dist = Distance(
    [santiago.latitud, santiago.longitud], [concepcion.latitud, concepcion.longitud]
).km()

if int(dist) == 500:
    print("Funciona")
else:
    print("Estas lejos compadre")
