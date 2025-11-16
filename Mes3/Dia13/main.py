"""
=== Desafio do Dia 73 — Analisador de Gastos Semanais (Pandas) ===

Descrição:
Neste desafio você continuará praticando manipulação de DataFrames com Pandas,
criando métricas úteis para analisar gastos semanais. O objetivo é exercitar
operações como criação de colunas derivadas, agrupamentos, estatísticas,
filtragens, ordenações e pequenas análises de padrão de consumo.

Objetivos:
 - Reforçar operações essenciais de Pandas
 - Criar métricas derivadas e classificações
 - Utilizar filtros, groupby e ordenações
 - Realizar análises úteis de um conjunto de dados simples
"""





import pandas as pd

dados = {
    "categoria": ["alimentação", "transporte", "lazer", "alimentação", "contas", "transporte", "lazer"],
    "valor": [32.5, 12.0, 45.0, 20.0, 80.0, 15.0, 30.0],
    "dia": ["Seg", "Seg", "Seg", "Ter", "Ter", "Qua", "Qua"]
}

df = pd.DataFrame(dados)



df["custo_relativo"] = df["valor"] / df["valor"].sum()
gastos_por_categoria = df.groupby("categoria")["valor"].sum()
media_por_dia = df.groupby("dia")["valor"].mean()

gastos_altos = df[df["valor"] > 30]
ordem_decrescente = df.sort_values(by="valor", ascending=False)
gasto_maximo = df.loc[df["valor"].idxmax()]
gasto_minimo = df.loc[df["valor"].idxmin()]

df["faixa"] = pd.cut(df["valor"], bins=[0,20,40,100], labels=["baixo","médio","alto"])

df_primeiros = df.iloc[:3]
total_semana = df["valor"].sum()





print("\n=-=- ANÁLISE DETALHADA =-=-\n", df)

print("\nDATAFRAME ORIGINAL:\n", df)
print("\nGastos totais por categoria:\n", gastos_por_categoria)
print("\nMédia de gastos por dia:\n", media_por_dia)
print("\nGastos acima de 30:\n", gastos_altos)
print("\nOrdenado por valor decrescente:\n", ordem_decrescente)
print("\nMaior gasto da semana:\n", gasto_maximo)
print("\nMenor gasto da semana:\n", gasto_minimo)
print("\nClassificação por faixa de valor:\n", df[["valor","faixa"]])
print("\nPrimeiros registros (iloc):\n", df_primeiros)
print("\nGasto total na semana:", total_semana)
