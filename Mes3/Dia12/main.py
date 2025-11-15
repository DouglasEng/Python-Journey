"""
=== Desafio do Dia 72 — Analisador de Hábitos de Estudo (Pandas) ===

Descrição:
Treinar conceitos fundamentais de Pandas, explorando operações práticas como criação
de colunas, estatísticas descritivas,agrupamentos, filtragens, seleção avançada e 
pequenas análises úteis do cotidiano. O objetivo é simular uma análise realista dos
hábitos de estudo de um aluno ao longo da semana.

Objetivos:
 - Praticar criação e manipulação de DataFrames
 - Trabalhar com groupby, describe, filtros e ordenações
 - Criar colunas derivadas e classificações
 - Explorar loc, iloc e operações de identificação de padrões
"""





import pandas as pd




dados = {
    "materia": ["Python", "Matemática", "Dados", "Python", "Matemática", "Dados", "Python"],
    "horas": [2, 1.5, 3, 2.5, 2, 4, 3],
    "dia": ["Seg", "Seg", "Seg", "Ter", "Ter", "Qua", "Qua"]
}

df = pd.DataFrame(dados)
print("\nDATAFRAME ORIGINAL:\n", df)

df["produtividade"] = df["horas"] * 10
print("\nProdutividade calculada:\n", df)

print("\nEstatísticas descritivas:")
print(df["horas"].describe())

print("\nHoras totais por matéria:")
print(df.groupby("materia")["horas"].sum())

print("\nHoras médias por dia:")
print(df.groupby("dia")["horas"].mean())

print("\nEstudos com mais de 2 horas:")
print(df[df["horas"] > 2])

print("\nMaior sessão de estudo:")
print(df.loc[df["horas"].idxmax()])

print("\n3 primeiras linhas (iloc):")
print(df.iloc[:3])

df_ordenado = df.sort_values(by="horas", ascending=False)
print("\nOrdenado por horas:")
print(df_ordenado)

df["ritmo"] = pd.cut(df["horas"], bins=[0,2,3.5,5], labels=["baixo","médio","alto"])
print("\nClassificação por ritmo de estudo:")
print(df)

print("\nDias onde estudou Python:")
print(df[df["materia"] == "Python"])

print("\nTotal de horas estudadas na semana:", df["horas"].sum())
