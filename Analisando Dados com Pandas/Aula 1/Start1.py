import pandas as pd

# python Start1.py

df_data = pd.read_csv("supermarket_sales.csv")

df_data.head()

# Total de faturamento por filial?
result = df_data.groupby("City")["Total"].sum()
print("result 1 = ", result)


print("----------------------------------")
result2 = df_data.groupby("City")[["Total", "gross income"]].sum()
print(result2)

print("----------------------------------")
# Qual o percentual de participação na receita de cada tipo de produto?

result3 = (df_data.groupby("Product line")["Total"].sum() / df_data.groupby("Product line")["Total"].sum().sum()).sort_values() * 100
print(result3)

print("----------------------------------")
# Como esta distribuído o tipo de produto consumido por genero?
result4 = df_data.groupby(["Product line", "Gender"])["Total"].sum()
print(result4)

result5 = df_data.groupby(["Product line", "Gender"])[["Total"]].sum().pivot_table(index="Product line", columns="Gender")
print(result5)

print("----------------------------------")
# Qual foi o faturamento por mês?
df_data["Date"] = pd.to_datetime(df_data["Date"])
df_data["Month"] = df_data["Date"].apply(lambda x: x.month)
df_data["Year"] = df_data["Date"].apply(lambda x: x.year)

result6 = df_data.groupby(["Month"])["Total"].sum()
print(result6)

print("----------------------------------")
# qual foi a média de avaliação por cada filial e, janeiro de 2019?
result7 = df_data[(df_data["Year"] ==2019) & (df_data["Month"] == 1)]["Rating"].mean()
print(result7)

print("----------------------------------")
# Como se distribui o gasto por tipo de consumidor em cada filial?
result8 = df_data.groupby(["Customer type", "City"])["Total"].sum()
print(result8)
