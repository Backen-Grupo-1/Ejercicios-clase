# Viento registrado en estaciones de monitoreo
# • Cree un programa que solicite el nombre de una estación de monitoreo y los vientos registrados (nudos) 
#   en las últimas 5, 10, y 15 horas.
# • Almacene esta información en la memoria principal usando diccionarios y listas.
# • Su programa debe crear un nuevo diccionario con los vientos registrados en kilómetros por hora.
# • Además, el programa debe mostrar por la salida estándar el nombre de la estación y los vientos registrados 
#   (convertidos a kilómetros por hora).
# • Debe usar operación map().
# • Tip: los vientos en una zona calmada están entre los 3 y 10 nudos.

estacion = input('Nombre de estación: ')

vientos = []
horas = ['5 horas', '10 horas', '15 horas']
for hora in horas:
    vientos.append(float(input(f"Ingrese los vientos registrados en las últimas {hora}: ")))

vientos_dic = {
    estacion: {
        'vientos': vientos,
        'kmh': list(map(lambda nudo: nudo * 1.8, vientos))
    }
}

for i in range(len(vientos)):
    print(f"Estación {estacion}: el viento registrado en las últimas {horas[i]} fue de {vientos_dic[estacion]['kmh'][i]} km/h ({vientos_dic[estacion]['vientos'][i]} nudos)")