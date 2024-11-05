# Valor absoluto
# • Escriba una función lambda que reciba un número y retorne su valor absoluto.
# • Recuerde que el valor absoluto realiza lo siguiente: si el número es positivo o cero, devuelve el mismo número; 
#   si el número es negativo, devuelve el mismo número pero como valor positivo.

valor_absoluto = lambda x: x if x >= 0 else -x

print(valor_absoluto(-5))