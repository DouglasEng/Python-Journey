"""
=== Desafio do Dia 82 — Pivot Tables e Operações Avançadas com Pandas ===

Objetivos:
 - Criar uma base de vendas com múltiplos produtos e regiões
 - Gerar métricas derivadas (faturamento, classificação e categorias)
 - Criar pivot tables úteis para análise
 - Aplicar transformações com lambda e funções personalizadas
"""







import pandas as pd
import numpy as np





def criar_base():
    np.random.seed(42)
    produtos = ["Copo", "Prato", "Tampa", "Talher"]
    regioes = ["Norte", "Sul", "Leste", "Oeste"]

    df = pd.DataFrame({
        "product": np.random.choice(produtos, 40),
        "region": np.random.choice(regioes, 40),
        "units_sold": np.random.randint(20, 250, 40),
        "unit_price": np.random.uniform(1.0, 5.0, 40).round(2)
    })
    df["revenue"] = df["units_sold"] * df["unit_price"]
    return df






def aplicar_transformacoes(df):
    df["category"] = df["units_sold"].apply(
        lambda x: "Alta demanda" if x > 150 else "Normal"
    )
    media_revenue = df["revenue"].mean()
    df["above_avg"] = df["revenue"].apply(
        lambda x: "Acima" if x > media_revenue else "Abaixo"
    )
    return df




def gerar_pivot_tables(df):
    p1 = pd.pivot_table(
        df,
        values="revenue",
        index="product",
        columns="region",
        aggfunc="sum",
        fill_value=0
    )

    p2 = pd.pivot_table(
        df,
        values="units_sold",
        index="region",
        aggfunc=["mean", "sum"]
    )

    p3 = pd.pivot_table(
        df,
        values="revenue",
        index="category",
        aggfunc=["mean", "count"]
    )

    return p1, p2, p3


def main():
    df = criar_base()
    print("\n=-=- BASE ORIGINAL =-=-")
    print(df)
    df = aplicar_transformacoes(df)
    print("\n=-= BASE COM TRANSFORMAÇÕES =-=")
    print(df)
    p1, p2, p3 = gerar_pivot_tables(df)
    print("\n=-= PIVOT TABLE — Revenue por produto vs região =-=")
    print(p1)
    print("\n=-= PIVOT TABLE — Estatisticas de vendas por região =-=")
    print(p2)
    print("\n=-= PIVOT TABLE — Revenue por categoria (Demanda) =-=")
    print(p3)






if __name__ == "__main__":
    main()
