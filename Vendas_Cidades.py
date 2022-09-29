import pandas as pd
import matplotlib.pyplot as plt

# ***Importando dados do Excel

df1 = pd.read_excel("C:\workspace\Bootcamp Unimed\ProjetoPythonPandas\datasets\Aracaju.xlsx")
df2 = pd.read_excel("C:\workspace\Bootcamp Unimed\ProjetoPythonPandas\datasets\Fortaleza.xlsx")
df3 = pd.read_excel("C:\workspace\Bootcamp Unimed\ProjetoPythonPandas\datasets\\Natal.xlsx")
df4 = pd.read_excel("C:\workspace\Bootcamp Unimed\ProjetoPythonPandas\datasets\Recife.xlsx")
df5 = pd.read_excel("C:\workspace\Bootcamp Unimed\ProjetoPythonPandas\datasets\Salvador.xlsx")

# Concatenando em um unico dataframe 
df = pd.concat([df1,df2,df3,df4,df5])

# *** Tratamento de Colunas
#Alterando o tipo de um campo
df["LojaID"] = df["LojaID"].astype("object")

#criando coluna calculada
df["Receita"] = df["Vendas"] * df["Qtde"]

# Criando colunas de dia, mes e ano a partir da data de venda
df["Dia_Venda"],df["Mes_Venda"],df["Ano_Venda"] = (df["Data"].dt.day, df["Data"].dt.month, df["Data"].dt.year)

# print(f'''***Primeiros registros***\n{df.head(2)} 
# ***Ultimosregistro***\n{df.tail(2)}
# ***Amostras de registros***\n{df.sample(10)}''') 

# Filtrando a venda de março de 2019
# print(df.loc[(df.Ano_Venda == 2019) & (df.Mes_Venda == 3)])

# Criando df para o ano 2019
df_2019 = df.loc[(df.Ano_Venda == 2019)]

# ***** Criando graficos
plt.style.use("ggplot")

## Graficos de barras
df_2019.LojaID.value_counts(ascending=False).plot.bar(title = "Quantidade de Venda X Loja", color = "green")
plt.xlabel("loja")
plt.ylabel("Total Vendas")
plt.show()

## Graficos de barras invertidas
df_2019.LojaID.value_counts(ascending=True).plot.barh(title = "Quantidade de Venda X Loja", color = "blue")
plt.ylabel("loja")
plt.xlabel("Total Vendas")
plt.show()

## Grafico de pizza
df_2019.groupby("Cidade")["Receita"].sum().plot.pie(title = "Ano 2019: Receita X Cidade")
plt.show()

## Grafico de linhas
df_2019.groupby("Mes_Venda")["Qtde"].sum().plot(marker = ".")
plt.title("Mês X Quantidade")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()
plt.show()

## Grafico de dispersão
plt.scatter(df_2019.Dia_Venda, df_2019.Receita)
plt.title("Dia X Venda")
plt.xlabel("Dia")
plt.ylabel("Total Receita")
plt.show()


















# *****Rascunhos

# # maiores de menores receitas 
# print(df.nlargest(5,["Receita"]))
# print(df.nsmallest(5,["Receita"]))

# Agrupando soma das receitas pelas cidades
# print(df.groupby("Cidade")["Receita"].sum())


# #Tipos de campos
# print(df.dtypes)

# #Exportando para excel
# conc = "C:\workspace\Bootcamp Unimed\ProjetoPythonPandas\datasets\concatenado.xlsx"
# df.to_excel(conc)
# conc_csv = "C:\workspace\Bootcamp Unimed\ProjetoPythonPandas\datasets\concatenado.csv"
# df.to_csv(conc_csv)

# print(df.sample(10))





