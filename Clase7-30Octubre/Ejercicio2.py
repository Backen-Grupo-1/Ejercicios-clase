import pandas as pd


datos = {
    "nombres": ["Juan", "María", "Pedro", "Ana", "Sofia"],
    "edades": [25, 30, 35, 40, 31],
    "rut": ["12345678-9", "98765432-1", "45678901-2", "23456789-0", "24565478-3"],
    "altura": [1.75, 1.68, 1.82, 1.70, 1.80],
    "peso": [70, 65, 80, 72, 67],
}

personas = pd.DataFrame(datos)

personas["rut_estandarizado"] = personas["rut"].str.split("-").str[0]
personas["digito_verificador"] = personas["rut"].str.split("-").str[1]

print(personas)
#   nombres  edades         rut  altura  peso rut_estandarizado digito_verificador
# 0    Juan      25  12345678-9    1.75    70          12345678                  9
# 1   María      30  98765432-1    1.68    65          98765432                  1
# 2   Pedro      35  45678901-2    1.82    80          45678901                  2
# 3     Ana      40  23456789-0    1.70    72          23456789                  0
# 4   Sofia      31  24565478-3    1.80    67          24565478                  3

personas["imc"] = personas["peso"] / (personas["altura"] ** 2)

personas["rango_edad"] = personas.apply(lambda x: "Mayor de 60" if (x["edades"] >= 60) else "Mayor de 30" if (x["edades"] >= 30) else "Menor de 30", axis=1)
print(personas)
