import pandas as pd


datos = {
    "nombres": ["Juan", "María", "Pedro", "Ana", "Sofia"],
    "edades": [25, 30, 35, 40, 31],
    "rut": ["12345678-9", "98765432-1", "45678901-2", "23456789-0", "24565478-3"],
    "altura": [1.75, 1.68, 1.82, 1.70, 1,80],
    "peso": [70, 65, 80, 72, 67]
}

personas = pd.DataFrame(datos)

head = personas.head()
#   nombres  edades         rut  altura  peso
# 0    Juan      25  12345678-9    1.75    70
# 1   María      30  98765432-1    1.68    65
# 2   Pedro      35  45678901-2    1.82    80
# 3     Ana      40  23456789-0    1.70    72

# print(head)
personas.info()

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4 entries, 0 to 3
# Data columns (total 5 columns):
#  #   Column   Non-Null Count  Dtype  
# ---  ------   --------------  -----  
#  0   nombres  4 non-null      object 
#  1   edades   4 non-null      int64  
#  2   rut      4 non-null      object 
#  3   altura   4 non-null      float64
#  4   peso     4 non-null      int64  
# dtypes: float64(1), int64(2), object(2)
# memory usage: 292.0+ bytes

# personas.describe()
describe = personas.describe()
#           edades    altura       peso
# count   4.000000  4.000000   4.000000
# mean   32.500000  1.737500  71.750000
# std     6.454972  0.062383   6.238322
# min    25.000000  1.680000  65.000000
# 25%    28.750000  1.695000  68.750000
# 50%    32.500000  1.725000  71.000000
# 75%    36.250000  1.767500  74.000000
# max    40.000000  1.820000  80.000000

# print(describe)
