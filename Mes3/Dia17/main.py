"""
=== Desafio do Dia 77 — Visualizações Avançadas do Dataset de E-commerce ===

Descrição:
A ideia é gerar gráficos úteis e interpretáveis, semelhantes aos 
utilizados em relatóriosexecutivos e dashboards de acompanhamento 
semanal.

Tarefas principais:
 - Criar visualizações para:
     • Receita por categoria de produto
     • Ticket médio por método de pagamento
     • Distribuição da idade dos clientes
     • Compras por hora do dia
     • Top 10 cidades em receita
     • Correlação entre preço e quantidade
 - Salvar todos os gráficos em arquivos .png na pasta atual
 - Ajustar títulos, rótulos, tamanho da figura e legibilidade

Objetivo didático:
Praticar a criação de gráficos profissionais com Pandas + Matplotlib,
interpretar padrões visuais e consolidar análises para apresentações futuras.
"""




import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os






pd.set_option("display.width", 180)
pd.set_option("display.max_columns", 50)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "ecommerce_dataset.csv")





df = pd.read_csv(FILENAME)
df["purchase_date"] = pd.to_datetime(df["purchase_date"], errors="coerce")
df["total_value"] = df["price"] * df["quantity"]
df["hour"] = df["purchase_date"].dt.hour
df["day"] = df["purchase_date"].dt.date
bins = [0, 17, 30, 45, 60, 200]
labels = ["0-17", "18-30", "31-45", "46-60", "61+"]
df["age_group"] = pd.cut(df["customer_age"], bins=bins, labels=labels)


#receita por categoria
fig, ax = plt.subplots(figsize=(10, 5))
df.groupby("product_category")["total_value"].sum().sort_values().plot(kind="barh", ax=ax)
ax.set_title("Receita Total por Categoria", fontsize=14)
ax.set_xlabel("Receita (R$)")
plt.tight_layout()
plt.savefig("dia77_receita_por_categoria.png")
plt.close()


# ticket medio por metodo de pagamento
fig, ax = plt.subplots(figsize=(8, 5))
df.groupby("payment_method")["total_value"].mean().sort_values().plot(kind="bar", ax=ax)
ax.set_title("Ticket Médio por Método de Pagamento", fontsize=14)
ax.set_ylabel("Ticket Médio (R$)")
plt.tight_layout()
plt.savefig("dia77_ticket_por_pagamento.png")
plt.close()




# histograga idade dos clientes
fig, ax = plt.subplots(figsize=(10, 5))
df["customer_age"].plot(kind="hist", bins=20)
ax.set_title("Distribuição da Idade dos Clientes", fontsize=14)
ax.set_xlabel("Idade")
plt.tight_layout()
plt.savefig("dia77_distribuicao_idade.png")
plt.close()



# comras por hora do dia

fig, ax = plt.subplots(figsize=(10, 5))
df["hour"].value_counts().sort_index().plot(kind="line", marker="o", ax=ax)
ax.set_title("Volume de Compras por Hora do Dia", fontsize=14)
ax.set_xlabel("Hora")
ax.set_ylabel("Número de Transações")
plt.grid(True, linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.savefig("dia77_compras_por_hora.png")
plt.close()



#10 cidades or receitas
fig, ax = plt.subplots(figsize=(12, 6))
df.groupby("city")["total_value"].sum().sort_values(ascending=False).head(10).plot(kind="bar", ax=ax)
ax.set_title("Top 10 Cidades por Receita", fontsize=14)
ax.set_ylabel("Receita (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("dia77_top10_cidades_receita.png")
plt.close()


#correlação entre preco e quantidade
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(df["price"], df["quantity"], alpha=0.4)
ax.set_title("Relação entre Preço e Quantidade", fontsize=14)
ax.set_xlabel("Preço")
ax.set_ylabel("Quantidade")
plt.tight_layout()
plt.savefig("dia77_correlacao_preco_quantidade.png")
plt.close()





print("\n-=-= ANÁLISE DOS DADOS EM GRÁFICOS ===")
print("Gráficos gerados com sucesso:")
print("- dia77_receita_por_categoria.png")
print("- dia77_ticket_por_pagamento.png")
print("- dia77_distribuicao_idade.png")
print("- dia77_compras_por_hora.png")
print("- dia77_top10_cidades_receita.png")
print("- dia77_correlacao_preco_quantidade.png")
print("\nOs arquivos PNG foram salvos no diretório atual.")
