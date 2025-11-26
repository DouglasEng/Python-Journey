"""
=== Desafio do Dia 83 — Análise da Hamburgueria Pandástica com Pandas ===

Descrição:
Este desafio trabalha Pandas em um contexto leve e descontraído: uma hamburgueria
fictícia com pedidos, horários, avaliações e perfis de clientes. A ideia é analisar
tendências, criar métricas, agrupar informações e gerar tabelas úteis.

Objetivos:
 - Criar uma base interna simulando pedidos de uma hamburgueria
 - Criar métricas derivadas (valor total, período do dia, satisfação)
 - Identificar produtos mais vendidos, horários mais lucrativos e perfis de consumo
 - Gerar pivot tables e agrupamentos úteis
 - Usar funções lambda e agregações personalizadas
"""







import pandas as pd
import numpy as np





def criar_base():
    np.random.seed(42)
    itens = ["Hamburguer Simples", "Hamburguer Duplo", "Batata Média", "Batata Grande",
             "Refrigerante", "Milkshake", "Nuggets", "Onion Rings"]
    metodo_pagamento = ["Pix", "Crédito", "Débito", "Dinheiro"]
    periodos = ["Manhã", "Tarde", "Noite"]

    df = pd.DataFrame({
        "item": np.random.choice(itens, 60),
        "quantidade": np.random.randint(1, 5, 60),
        "preco_unit": np.random.uniform(8, 35, 60).round(2),
        "hora_pedido": np.random.randint(8, 23, 60),
        "metodo_pagamento": np.random.choice(metodo_pagamento, 60),
        "nota_cliente": np.random.randint(1, 6, 60)  # 1 a 5
    })

    df["valor_total"] = df["quantidade"] * df["preco_unit"]
    df["periodo"] = df["hora_pedido"].apply(
        lambda h: "Manhã" if h < 12 else ("Tarde" if h < 18 else "Noite")
    )
    df["satisfacao"] = df["nota_cliente"].apply(
        lambda n: "Satisfeito" if n >= 4 else ("Neutro" if n == 3 else "Insatisfeito")
    )
    return df





def analises(df):
    mais_vendidos = df["item"].value_counts()
    fat_por_periodo = df.groupby("periodo")["valor_total"].sum()
    ticket_pagamento = df.groupby("metodo_pagamento")["valor_total"].mean()
    avaliacao_por_item = df.groupby("item")["nota_cliente"].mean().sort_values(ascending=False)
    distribuicao_satisfacao = df["satisfacao"].value_counts(normalize=True)
    return (mais_vendidos, fat_por_periodo, ticket_pagamento,
            avaliacao_por_item, distribuicao_satisfacao)





def gerar_pivots(df):
    p1 = pd.pivot_table(
        df,
        values="valor_total",
        index="item",
        columns="periodo",
        aggfunc="sum",
        fill_value=0
    )
    p2 = pd.pivot_table(
        df,
        values="nota_cliente",
        index="periodo",
        columns="metodo_pagamento",
        aggfunc="mean",
        fill_value=0
    )
    return p1, p2







def main():
    df = criar_base()
    print("\n=-=- BASE INICIAL -=-=")
    print(df)

    (mv, fat, tik, aval, satis) = analises(df)

    print("\n=-= ITENS MAIS VENDIDOS =-=")
    print(mv)
    print("\n=-= FATURAMENTO POR PERÍODO =-=")
    print(fat)
    print("\n=-= TICKET MÉDIO POR MÉTODO DE PAGAMENTO =-=")
    print(tik)

    print("\n=-= MÉDIA DE AVALIAÇÃO POR ITEM =-=")
    print(aval)
    print("\n=-= DISTRIBUIÇÃO DE SATISFAÇÃO =-=")
    print(satis)

    p1, p2 = gerar_pivots(df)

    print("\n=-= PIVOT — Faturamento por Item vs P=período =-=")
    print(p1)
    print("\n=-= PIVOT — Média de notas por P=período vs P=pagamento =-=")
    print(p2)







if __name__ == "__main__":
    main()
