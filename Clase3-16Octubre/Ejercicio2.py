# Función distancia como “lambda”
# • Escriba nuevamente la función de distancia euclidiana.
# • Transforme la función a una función anónima (lambda).
# • Su programa debe recibir las coordenadas por la entrada estándar y luego llamar a la función anónima.
# • La función anónima debe retornar la distancia euclidiana (presente el resultado por la salida estándar).

distancia_euclidiana = lambda x1, y1, x2, y2: ((x2 - x1)**2 + (y2 - y1)**2)**0.5

x1 = int(input("Ingrese x1: "))
y1 = int(input("Ingrese y1: "))
x2 = int(input("Ingrese x2: "))
y2 = int(input("Ingrese y2: "))

print(f"La distancia euclidiana es: {distancia_euclidiana(x1, y1, x2, y2):.2f}")