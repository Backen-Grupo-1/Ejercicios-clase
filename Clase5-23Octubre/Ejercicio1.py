try:
    frutas = ["manzana", "pera", "platano", "sandia"]

    # print(frutas[4])

    comida = {
        "frutas": ["manzana", "pera", "platano", "sandia"]
    }
    print(comida["verduras"])

except IndexError as e:

    print("Error: ", e)

except KeyError as e:

    print("Error: ", str(type(e)))




