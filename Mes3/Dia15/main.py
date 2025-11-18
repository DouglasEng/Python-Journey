"""
=== Desafio do Dia 75 — Análise Prática de E-commerce com Pandas ===

Descrição:
Usando o arquivo de transações fornecido (ecommerce_dataset.csv), este desafio
pede uma análise prática e estruturada com Pandas. A ideia é executar uma sequência lógica:
carregar, limpar/transformar, extrair métricas relevantes e gerar um resumo que possa ser
usado em relatórios de negócio.

Tarefas principais:
 - Carregar o CSV e tratar tipos (datas, numéricos)
 - Criar colunas derivadas (total_price, year/month/day/hour)
 - Verificar qualidade dos dados (nulos, tipos, valores extremos)
 - Responder perguntas de negócio:
     • Categorias mais lucrativas
     • Cidades que mais geram receita
     • Ticket médio por método de pagamento
     • Distribuição da idade dos clientes + faixas etárias
     • Detecção de transações outliers
 - Criar agregações úteis e exportar um resumo em CSV
"""




import pandas as pd
import numpy as np

import os




BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "ecommerce_dataset.csv")

pd.set_option("display.width", 180)
pd.set_option("display.max_columns", 50)




def carregar_e_preparar(path):
    df = pd.read_csv(path)

    df["purchase_date"] = pd.to_datetime(df["purchase_date"], errors="coerce")

    colunas_numericas = ["price", "quantity", "customer_age"]
    for c in colunas_numericas:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    df["total_price"] = df["price"] * df["quantity"]

    if pd.api.types.is_datetime64_any_dtype(df["purchase_date"]):
        df["year"] = df["purchase_date"].dt.year
        df["month"] = df["purchase_date"].dt.month
        df["day"] = df["purchase_date"].dt.day
        df["hour"] = df["purchase_date"].dt.hour
        df["weekday"] = df["purchase_date"].dt.day_name()

    return df







def relatorio_qualidade(df):
    print("\n=-= RELATÓRIO DE QUALIDADE DOS DADOS =-=")
    print("Dimensões:", df.shape)
    print("\nTipos das colunas:\n", df.dtypes)
    print("\nValores nulos:\n", df.isna().sum())
    print("\nEstatísticas básicas:\n", df[["price", "quantity", "total_price", "customer_age"]].describe())






def categorias_mais_lucrativas(df, n=5):
    return df.groupby("product_category")["total_price"].sum().sort_values(ascending=False).head(n)


def cidades_com_mais_receita(df, n=5):
    return df.groupby("city")["total_price"].sum().sort_values(ascending=False).head(n)


def ticket_por_pagamento(df):
    tabela = df.groupby("payment_method")["total_price"].agg(["mean", "median", "count"])
    tabela.columns = ["ticket_medio", "ticket_mediano", "quantidade_transacoes"]
    return tabela.sort_values("ticket_medio", ascending=False)


def distribuicao_faixas_etarias(df):
    faixas = [0, 18, 25, 35, 45, 60, 120]
    labels = ["<18", "18-24", "25-34", "35-44", "45-59", "60+"]

    df["faixa_etaria"] = pd.cut(df["customer_age"], bins=faixas, labels=labels)
    dist = df["faixa_etaria"].value_counts().reindex(labels, fill_value=0)
    return dist, df


def receita_por_horario_e_dia(df):
    receita_horaria = df.groupby("hour")["total_price"].sum()
    receita_semana = df.groupby("weekday")["total_price"].sum().reindex(
        ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], fill_value=0
    )
    return receita_horaria, receita_semana



def detectar_outliers(df):
    valores = df["total_price"].dropna()
    media = valores.mean()
    desvio = valores.std()
    limite = media + 3 * desvio

    outliers = df[df["total_price"] > limite].sort_values("total_price", ascending=False)
    return outliers, media, desvio, limite


def metricas_por_categoria(df):
    tabela = df.groupby("product_category").agg(
        receita_total=("total_price", "sum"),
        total_transacoes=("transaction_id", "count"),
        ticket_medio=("total_price", "mean"),
        media_quantidade=("quantity", "mean")
    )
    return tabela.sort_values("receita_total", ascending=False)




def salvar_resumo(df, nome="resumo_dia15.csv"):
    resumo = {
        "qtd_transacoes": len(df),
        "receita_total": float(df["total_price"].sum()),
        "ticket_medio": float(df["total_price"].mean()),
    }

    top3 = categorias_mais_lucrativas(df, 3)
    resumo["top3_categorias"] = ";".join([f"{cat}:{valor:.2f}" for cat, valor in top3.items()])
    pd.Series(resumo).to_csv(nome)
    return nome








df = carregar_e_preparar(FILENAME)

relatorio_qualidade(df)

print("\n=-= CATEGORIAS MAIS LUCRATIVAS =-=")
print(categorias_mais_lucrativas(df))
print("\n=-= CIDADES COM MAIOR RECEITA =-=")
print(cidades_com_mais_receita(df))
print("\n=-= TICKET MÉDIO POR MÉTODO DE PAGAMENTO =-=")
print(ticket_por_pagamento(df))

dist_etaria, df = distribuicao_faixas_etarias(df)
print("\n=-= DISTRIBUIÇÃO POR FAIXAS ETÁRIAS =-=")
print(dist_etaria)

print("\n=-= RECEITA POR HORA E POR DIA DA SEMANA =-=")
horas, dias = receita_por_horario_e_dia(df)
print("\nReceita por hora:\n", horas.sort_index())
print("\nReceita por dia da semana:\n", dias)
outliers, media, desvio, limite = detectar_outliers(df)
print("\n=-= DETECÇÃO DE OUTLIERS =-=")
print(f"Média: {media:.2f}")
print(f"Desvio padrão: {desvio:.2f}")
print(f"Limite (> média + 3*desvio): {limite:.2f}")
print(f"Quantidade de outliers: {len(outliers)}")

if len(outliers) > 0:
    print("\nTop outliers:")
    print(outliers[["transaction_id", "customer_id", "product_category", "total_price", "payment_method", "city"]].head(10))

print("\n=-= MÉTRICAS POR CATEGORIA =-=")
print(metricas_por_categoria(df))

arquivo = salvar_resumo(df)
print(f"\nResumo salvo em: {arquivo}")

print("\n=-= FINALIZADO =-=")
print("Use este conjunto de dados para os próximos desafios (75.2 e 75.3).")
