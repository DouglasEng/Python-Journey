"""
=== Desafio do Dia 78 — Análise com Pandas sem Base Externa ===

Descrição:
A ideia é manter o ritmo das análises do Day 75–77: criar um DataFrame,
construir colunas derivadas e extrair métricas relevantes de negócio.

Tarefas:
 - Criar manualmente um DataFrame com informações de vendas
 - Incluir colunas como: product, price, quantity, category, age, payment
 - Gerar coluna derivada total_price
 - Realizar análises:
     • Receita por categoria
     • Idade média dos clientes
     • Produto mais vendido (quantidade)
     • Ticket médio geral
 - Exibir um relatório final no terminal
"""

import pandas as pd

def criar_base():
    data = {
        "product": [
            "Teclado", "Mouse", "Monitor", "Headset", "Mouse", "Webcam",
            "Teclado", "Cadeira", "Headset", "Monitor", "Mousepad", "Mousepad"
        ],
        "price": [120, 60, 900, 150, 60, 200, 120, 850, 150, 900, 40, 40],
        "quantity": [1, 2, 1, 1, 3, 1, 2, 1, 1, 2, 3, 1],
        "category": [
            "Periféricos", "Periféricos", "Monitores", "Periféricos",
            "Periféricos", "Câmeras", "Periféricos", "Móveis", "Periféricos",
            "Monitores", "Acessórios", "Acessórios"
        ],
        "customer_age": [22, 34, 29, 19, 41, 27, 33, 30, 24, 28, 26, 37],
        "payment_method": [
            "Pix", "Crédito", "Crédito", "Pix", "Débito", "Crédito",
            "Pix", "Crédito", "Pix", "Crédito", "Débito", "Pix"
        ]
    }

    df = pd.DataFrame(data)
    df["total_price"] = df["price"] * df["quantity"]
    return df






def analisar(df):
    print("\n=-= Analises =-=")

    print("\n1) Receita por categoria:")
    print(df.groupby("category")["total_price"].sum())
    print("\n2) Idade média dos clientes:")
    print(df["customer_age"].mean())
    print("\n3) Produto mais vendido (em quantidade):")
    mais_vendido = df.groupby("product")["quantity"].sum().sort_values(ascending=False).head(1)
    print(mais_vendido)



    print("\n4) Ticket médio geral:")
    print(df["total_price"].mean())





def main():
    df = criar_base()
    print("\n=-=- DataFrame criado =-=-")
    print(df)
    analisar(df)





if __name__ == "__main__":
    main()
