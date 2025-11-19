"""
=== Desafio do Dia 76 — Análises Avançadas do Dataset de E-commerce ===

Descrição:
O objetivo é simular análises reais utilizadas em relatórios internos
de empresas: comportamento de faixas etárias, tendências por cidade,
diferenças entre métodos de pagamento e padrões relacionados ao horário
e ao dia das compras.

Tarefas principais:
 - Criar novas colunas derivadas (total_value, faixas etárias)
 - Analisar receita total, categorias e quantidades vendidas
 - Explorar comportamento de compra por faixa etária
 - Identificar cidades mais relevantes (transações, receita, ticket)
 - Avaliar métodos de pagamento e preferências por público
 - Detectar padrões temporais (hora e dia)
 - Identificar outliers de preço usando IQR
"""





import pandas as pd
import numpy as np

pd.set_option("display.width", 180)
pd.set_option("display.max_columns", 50)


df = pd.read_csv("ecommerce_dataset.csv")





df["purchase_date"] = pd.to_datetime(df["purchase_date"], errors="coerce")
df["total_value"] = df["price"] * df["quantity"]

bins = [0, 17, 30, 45, 60, 200]
labels = ["0-17", "18-30", "31-45", "46-60", "61+"]
df["age_group"] = pd.cut(df["customer_age"], bins=bins, labels=labels, right=True)

receita_total = df["total_value"].sum()
receita_por_categoria = df.groupby("product_category")["total_value"].sum().sort_values(ascending=False)
quantidade_por_categoria = df.groupby("product_category")["quantity"].sum().sort_values(ascending=False)
compras_por_faixa = df.groupby("age_group")["transaction_id"].count().sort_values(ascending=False)
ticket_por_faixa = df.groupby("age_group")["total_value"].mean().sort_values(ascending=False)
categoria_por_faixa = pd.crosstab(df["age_group"], df["product_category"])

top_transacoes_cidade = df["city"].value_counts().head(5)
top_receita_cidade = df.groupby("city")["total_value"].sum().sort_values(ascending=False).head(5)
ticket_por_cidade = df.groupby("city")["total_value"].mean().sort_values(ascending=False).head(5)

metodo_mais_usado = df["payment_method"].value_counts()
receita_por_metodo = df.groupby("payment_method")["total_value"].sum().sort_values(ascending=False)
ticket_por_metodo = df.groupby("payment_method")["total_value"].mean().sort_values(ascending=False)
preferencia_metodo_faixa = df.groupby(["payment_method", "age_group"])["total_value"].count()

df["hour"] = df["purchase_date"].dt.hour
df["day"] = df["purchase_date"].dt.date

compras_por_hora = df["hour"].value_counts().sort_index()
compras_por_dia = df["day"].value_counts().head(10)
categoria_por_hora = df.groupby(["hour", "product_category"])["transaction_id"].count().unstack(fill_value=0)

Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)
IQR = Q3 - Q1
lim_inf = Q1 - 1.5 * IQR
lim_sup = Q3 + 1.5 * IQR

outliers_df = df[(df["price"] < lim_inf) | (df["price"] > lim_sup)]
outliers_total = len(outliers_df)
outliers_por_categoria = outliers_df["product_category"].value_counts()








print("\n=-=- ANALISE DETALHADA =-=")

print("\n=-= Receita total =-=")
print(receita_total)

print("\n=-= Receita por categoria =-=")
print(receita_por_categoria)

print("\n=-= Quantidade vendida por categoria =-=")
print(quantidade_por_categoria)

print("\n=-= Compras por faixa etaria =-=")
print(compras_por_faixa)

print("\n=-= Ticket médio por faixa etaria =-=")
print(ticket_por_faixa)

print("\n=-= Preferência de categoria por faixa etaria =-=")
print(categoria_por_faixa)

print("\n=-= Top 5 cidades (Transações) =-=")
print(top_transacoes_cidade)

print("\n=-= Top 5 cidades (Receita) =-=")
print(top_receita_cidade)

print("\n=-= Ticket médio por cidade =-=")
print(ticket_por_cidade)

print("\n=-= Métodos de pagamento mais usados =-=")
print(metodo_mais_usado)

print("\n=-= Receita por método de pagamento =-=")
print(receita_por_metodo)

print("\n=== Ticket médio por método de pagamento =-=")
print(ticket_por_metodo)

print("\n=-= Preferência de metodo por faixa etaria ===")
print(preferencia_metodo_faixa)

print("\n=-= Compras por hora =-=")
print(compras_por_hora)

print("\n=-= Dias com mais vendas =-=")
print(compras_por_dia)

print("\n=-= Categorias compradas por hora =-=")
print(categoria_por_hora)

print("\n=-= Quantidade de preços outliers =-=")
print(outliers_total)

print("\n=-= Outliers por categoria =-=")
print(outliers_por_categoria)
