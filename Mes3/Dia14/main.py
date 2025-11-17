"""
=== Desafio do Dia 74 — Análise de Desempenho Semanal (Pandas) ===

Descrição:
Neste desafio você irá analisar um conjunto de dados simulando o desempenho
físico semanal de uma pessoa em diferentes exercícios. O objetivo é continuar
evoluindo no uso de Pandas aplicando operações como: criação de colunas
calculadas, agrupamentos, estatísticas, filtragens avançadas e identificação
de padrões ao longo do tempo.

Objetivos:
 - Reforçar criação de métricas a partir de colunas
 - Utilizar groupby para resumos estatísticos
 - Aplicar filtros condicionais múltiplos
 - Ordenar, selecionar e analisar padrões de progresso
"""



import pandas as pd

dados = {
    "dia": ["Seg", "Seg", "Ter", "Ter", "Qua", "Qua", "Qui", "Qui", "Sex", "Sex"],
    "exercicio": ["corrida", "musculação", "corrida", "yoga", "musculação", "corrida", "yoga", "musculação", "corrida", "yoga"],
    "duracao_min": [30, 45, 22, 40, 50, 28, 35, 60, 33, 42],
    "intensidade": [7, 8, 6, 5, 9, 7, 6, 8, 7, 5]
}

df = pd.DataFrame(dados)





df["carga_relativa"] = df["duracao_min"] * df["intensidade"]

media_por_exercicio = df.groupby("exercicio")[["duracao_min", "intensidade", "carga_relativa"]].mean()
dias_maior_carga = df[df["carga_relativa"] > df["carga_relativa"].mean()]
ordem_carga = df.sort_values(by="carga_relativa", ascending=False)
top_exercicio = media_por_exercicio["carga_relativa"].idxmax()
exercicio_mais_pesado = df[df["exercicio"] == top_exercicio]
progresso_corrida = df[df["exercicio"] == "corrida"].sort_values("duracao_min")
dia_de_maior_esforco = df.loc[df["carga_relativa"].idxmax()]
dia_de_menor_esforco = df.loc[df["carga_relativa"].idxmin()]




df["categoria_dia"] = pd.cut(
    df["carga_relativa"],
    bins=[0, 200, 350, 600],
    labels=["leve", "moderado", "pesado"]
)



print("\n=-=- ANALISE DETALHADA =-=-\n", df)

print("\nDATAFRAME ORIGINAL:\n", df)
print("\nMédia por exercício:\n", media_por_exercicio)
print("\nDias com carga acima da média:\n", dias_maior_carga)
print("\nRegistros ordenados por carga relativa:\n", ordem_carga)
print("\nExercício com maior média de carga relativa:", top_exercicio)
print("\nRegistros do exercício mais pesado:\n", exercicio_mais_pesado)
print("\nProgresso da corrida (ordenado por duração):\n", progresso_corrida)
print("\nDia de maior esforço:\n", dia_de_maior_esforco)
print("\nDia de menor esforço:\n", dia_de_menor_esforco)
print("\nClassificação de intensidade dos dias:\n", df[["dia","exercicio","categoria_dia"]])
