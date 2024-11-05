FIN = False
listado_llamados = []

while not FIN:
    frecuencia = input("Ingrese frecuencia: ")
    if frecuencia == "FIN":
        FIN = True
    else:
        motivo = input("Ingrese motivo: ")
        fecha = input("Ingrese fecha: ")
        registro_llamado = {"frecuencia": None, "motivo": None, "fecha": None}
        listado_llamados.append(registro_llamado)
print(listado_llamados)