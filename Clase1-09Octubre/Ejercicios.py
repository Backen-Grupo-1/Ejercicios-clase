#Trabajo grupal - Bloque A ---------------------------------------------------------------------------

#Ejercicio 1
numero_entrada = int(input("Ingrese un número: "))
if numero_entrada <= 0:
    print("No se puede calcular la raiz cuadrada de un numero negativo")
else:
    raiz_cuadrada = numero_entrada ** 0.5
    print(raiz_cuadrada)

#Ejercicio 2
x1 = int(input("Ingrese la coordenada x1: "))
x2 = int(input("Ingrese la coordenada x2: "))
y1 = int(input("Ingrese la coordenada y1: "))
y2 = int(input("Ingrese la coordenada y2: "))

distancia_euclidiana = ((x2-x1)**2 + (y2-y1)**2)**0.5
print(f"La distancia euclidiana es: {distancia_euclidiana}.")

#Ejercicio 3
palabra = input("Ingrese una palabra: ")
palabra_invertida = palabra[::-1]
print(f"La palabra original es: {palabra}, la palabra invertida es: {palabra_invertida}")


#Trabajo grupal - Bloque B ---------------------------------------------------------------------------

#Ejercicio 1

def raiz_cuadrada(numero):
    print(numero ** 0.5)

raiz_cuadrada(4)

#Ejercicio 2
palabra = str(input("Ingrese palabra: "))

if palabra == palabra[::-1]:
    print("Es palindromo")
else:
    print("No es palindromo")

#Ejercicio 3
def Num_Mayor(Num_Test, Valor_inf, Valor_sup):
    if Num_Test >= Valor_inf and Num_Test <= Valor_sup:
        return True
    else:
        return False
print(Num_Mayor(12,3,25))
print(Num_Mayor(50,3,25))

#Ejercicio 4
mayor = float("-inf")

FIN = False
while not FIN:
    valor = input()    
    if valor == "FIN":
        FIN = True
    else:
        if float(valor) > mayor:
            mayor = float(valor)
    print("Mayor hasta ahora es", mayor)
