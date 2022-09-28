import pandas as pd
import matplotlib.pyplot as plt

arquivo = "C:\workspace\Bootcamp Unimed\ProjetoPythonPandas\datasets\Gapminder.csv"
df = pd.read_csv(arquivo, sep=";")
df = df.rename(columns={"country":"País", "continent":"Continente", "year": "Ano", "lifeExp":"Expectativa_Vida","gdpPercap":"PIBperCapita", "pop":"Populacao_Total"})

print(df.head())

# dados estatisticos do DF
print(df.describe())

# mostra os valores distintos da coluna
print(df["Continente"].unique())

# total linhas e colunas
print(df.shape)

# Group by por continente e quantidade de paises
print(df.groupby("Continente")["País"].nunique())

# Group by por Ano 2007 e media de expectativa de vida
print(df.loc[df["Ano"]==2007].groupby("Ano")["Expectativa_Vida"].mean())

# #Grafico de barras 
df["PIBperCapita"].value_counts(ascending=False).plot.bar()
plt.show()






