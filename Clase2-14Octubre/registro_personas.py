"""
Registro de personas (Lista de diccionarios)

Desarrolla un programa que permita registrar el nombre y apellido de varias personas,
almacenando cada registro en un diccionario y organizando todos los registros en
una lista.
a. Solicita al usuario los datos de cada persona. Cada persona debe ser
almacenada en un diccionario con las claves "nombre" y "apellido".
b. Guarda cada diccionario en una lista llamada personas. Cada vez que se
ingresen los datos de una persona, crea un diccionario y agrégalo a la lista
personas.
c. El programa debe continuar solicitando datos hasta que el usuario ingrese "FIN"
como nombre.
d. Mostrar la lista de personas. Recorre la lista personas e imprime el nombre y
apellido de cada persona registrada.
"""

personas = []
flag = True
while flag:
    persona = {"nombre" : "", "apellido" : "", "cursos" : {} }
    nombre = input("Introduce nombre: ")
    if nombre == "FIN":
        flag = False
    else:
        apellido = input("Introduce apellido: ")
        persona["nombre"] = nombre
        persona["apellido"] = apellido
        curso = input("Introduce el nombre del curso: ")
        lista_notas = []
        for nota in range(3):
            notas = float(input("Introduce la nota: "))
            lista_notas.append(notas)
        persona["cursos"][curso] = lista_notas
        personas.append(persona)

for persona in personas:
    print(f"Mi nombre es: {persona["nombre"]} y mi apellido es: {persona["apellido"]}")
    for curso, nota in persona["cursos"].items():
        print(f"curso: {curso}, promedio de notas: {sum(nota)/len(nota)}")


"""
Cursos y notas de una persona
Incrementar la funcionalidad del programa anterior permitiendo que ahora cada
persona cuente con cursos inscritos.
• Es decir, necesitamos que cada persona contenga un diccionario con claves
correspondientes a cursos y cada clave con una lista con las notas de dicho
curso.
• Todos los datos deben ser solicitados por la entrada estándar. Puede considerar
ingresar un curso por persona. Cada curso tendrá 3 notas.
• Al finalizar, el programa debe imprimir el nombre y apellido, seguido del listado de
cursos y los promedios obtenidos en cada curso."""
