# Viento registrado en estaciones de monitoreo
# • Modifique el programa anterior para mostrar por pantalla los vientos que sobrepasan los 20 kilómetros por hora.
# • Utilice una operación filter() para complementar el ejercicio anterior de tal manera que pueda dar cumplimiento 
#   a los requisitos de este ejercicio.

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

vientos_sobre_20 = list(filter(lambda i: vientos_dic[estacion]['kmh'][i] > 20, range(len(vientos_dic[estacion]['kmh']))))

print(f"Vientos sobre 20 km/h")
for i in vientos_sobre_20:
    print(f"Estación {estacion}: el viento registrado en las últimas {horas[i]} fue de {vientos_dic[estacion]['kmh'][i]} km/h ({vientos_dic[estacion]['vientos'][i]} nudos)")