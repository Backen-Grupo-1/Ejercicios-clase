import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')
# print(df.head())

# sns.countplot(data=df, x='Survived')
# plt.title('Distribución de Supervivencia')
# plt.xlabel('Supervivencia (0 = No, 1 = Sí)')
# plt.ylabel('Cantidad de Pasajeros')
# plt.show()

# sns.histplot(data=df, x='Age', hue='Survived', multiple='stack', kde=True)
# plt.title('Distribución de Edad por Supervivencia')
# plt.xlabel('Edad')
# plt.ylabel('Cantidad')
# plt.show()

# sns.countplot(data=df, x='Pclass', hue='Survived')
# plt.title('Supervivencia según Clase de Pasajero')
# plt.xlabel('Clase (1 = Primera, 2 = Segunda, 3 = Tercera)')
# plt.ylabel('Cantidad')
# plt.show()

# sns.boxplot(data=df, x='Pclass', y='Fare')
# plt.title('Distribución de Tarifas por Clase')
# plt.xlabel('Clase')
# plt.ylabel('Tarifa')
# plt.show()

# sns.countplot(data=df, x='Sex', hue='Survived')
# plt.title('Supervivencia según Sexo')
# plt.xlabel('Sexo')
# plt.ylabel('Cantidad')
# plt.show()

# sns.scatterplot(data=df, x='Age', y='Fare', hue='Survived')
# plt.title('Relación entre Edad y Tarifa Pagada')
# plt.xlabel('Edad')
# plt.ylabel('Tarifa')
# plt.show()

# sns.countplot(data=df, x='Embarked', hue='Survived')
# plt.title('Supervivencia según Puerto de Embarque')
# plt.xlabel('Puerto de Embarque')
# plt.ylabel('Cantidad')
# plt.show()

# sns.histplot(data=df, x='SibSp', hue='Survived', multiple='stack', kde=True)
# plt.title('Supervivencia según Hermanos o Cónyuges a bordo')
# plt.xlabel('Cantidad de Hermanos/Cónyuges')
# plt.ylabel('Cantidad')
# plt.show()

# sns.histplot(data=df, x='Parch', hue='Survived', multiple='stack', kde=True)
# plt.title('Supervivencia según Padres o Hijos a bordo')
# plt.xlabel('Cantidad de Padres/Hijos')
# plt.ylabel('Cantidad')
# plt.show()

