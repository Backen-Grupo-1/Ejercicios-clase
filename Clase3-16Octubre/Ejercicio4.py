# Determinar el mayor valor en una lista
# • Escriba un programa que reciba una lista y permita determinar el valor mayor.
# • Debe usar una operación tipo “reduce()” para realizar las comparaciones.
# • El programa debe imprimir por pantalla el valor mayor de la lista.

from functools import reduce

lista = [4, 5, 2, 7, 9, 56, 10]

mayor_valor = reduce(lambda a, b: a if a > b else b, lista)

print(mayor_valor)