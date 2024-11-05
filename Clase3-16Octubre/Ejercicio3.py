# Dígito verificador en un RUT
# • Escriba una función lambda que retorne el dígito verificador de un RUT.
# • La lambda debe recibir como parámetro un RUT sin dígito verificador y retornar
#   este último.
# • Revise el algoritmo para dígito verificador en: https://es.wikipedia.org/wiki/Rol_%C3%9Anico_Tributario 
#   (sección “Procedimiento para obtener el dígito verificador”.

rut = '11111111'

# suma = 0
# for i in range(len(rut)):
#     # print(int(rut[::-1][i]))
#     # print((2 + i % 6))
#     suma = suma + int(rut[::-1][i]) * (2 + i % 6)

# print(11 - (suma % 11))

calcular_dv = lambda rut: 'K' if (dv := 11 - (sum(int(rut[::-1][i]) * (2 + i % 6) for i in range(len(rut)))) % 11) == 10 else 0 if dv == 11 else dv
print(f"El rut completo es {rut}-{calcular_dv(rut)}")
