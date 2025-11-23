"""
=== Desafio do Dia 80 — Controle de Produção com Pandas (sem CSV) ===

Descrição:
Este desafio continua o estudo progressivo de Pandas utilizando uma base criada
manualmente no código, sem arquivos externos. A proposta é simular o controle
semanal de produção de uma pequena fábrica, permitindo a prática de operações
como criação de colunas derivadas, agrupamentos, filtros e ordenação, gerando
um relatório final útil para tomada de decisões.

Tarefas:
 - Criar manualmente um DataFrame com dados de produção
 - Calcular produção total por produto
 - Calcular custo total por equipe
 - Determinar o produto mais barato de produzir
 - Identificar a equipe com menor taxa média de defeito
 - Filtrar dias com defeito acima de 5%
 - Ordenar equipes por produtividade total (ranking)
"""





import pandas as pd

def criar_base():
    data = {
        "day": ["Seg", "Seg", "Ter", "Ter", "Qua", "Qua", "Qui", "Qui", "Sex", "Sex"],
        "product": [
            "Copo", "Prato", "Copo", "Tampa",
            "Prato", "Tampa", "Copo", "Prato",
            "Tampa", "Copo"
        ],
        "units_produced": [120, 80, 140, 100, 70, 60, 160, 90, 110, 180],
        "unit_cost":       [0.70, 0.95, 0.70, 1.20, 0.95, 1.20, 0.70, 0.95, 1.20, 0.70],
        "defect_rate":     [3.2, 4.1, 2.5, 6.0, 3.8, 5.5, 1.9, 4.0, 7.3, 2.1],
        "team":            ["A", "B", "A", "C", "B", "C", "A", "B", "C", "A"]
    }
    df = pd.DataFrame(data)
    df["total_cost"] = df["units_produced"] * df["unit_cost"]

    return df





def analisar(df):
    print("\n=-= 1) Produção total por produto =-=")
    print(df.groupby("product")["units_produced"].sum())

    print("\n=-= 2) Custo total por equipe =-=")
    print(df.groupby("team")["total_cost"].sum().round(2))

    print("\n=-= 3) Produto mais barato de produzir (em média) =-=")
    print(df.groupby("product")["unit_cost"].mean().sort_values().head(1))

    print("\n=-= 4) Equipe com menor taxa média de defeito =-=")
    print(df.groupby("team")["defect_rate"].mean().sort_values().head(1))

    print("\n=-= 5) Dias com defeito acima de 5% =-=")
    print(df[df["defect_rate"] > 5])

    print("\n=-= 6) Ranking de produtividade por equipe =-=")
    ranking = df.groupby("team")["units_produced"].sum().sort_values(ascending=False)
    print(ranking)





def main():
    df = criar_base()
    print("\n=-=- Base Criada =-=-")
    print(df)
    analisar(df)





if __name__ == "__main__":
    main()
