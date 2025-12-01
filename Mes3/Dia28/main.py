"""
=== Desafio do Dia 88 — Análise de Rotina Semanal com Pandas ===

Descrição:
O objetivo é praticar leitura de CSV, agrupamentos, estatísticas básicas,
média semanal e criação de um relatório simples com Pandas.

Tarefas:
 - Carregar a base
 - Somar minutos por atividade
 - Somar minutos por dia
 - Identificar a atividade com maior carga total
 - Calcular a média semanal de minutos de estudo
 - Exibir um relatório final
"""




import pandas as pd
import os





BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "tarefas_semana.csv")
df = pd.read_csv(FILENAME)



total_por_atividade = df.groupby("atividade")["minutos"].sum().sort_values(ascending=False)
total_por_dia = df.groupby("dia")["minutos"].sum()
atividade_mais_tempo = total_por_atividade.idxmax()
minutos_atividade_mais = total_por_atividade.max()
df["semana"] = (df.index // 7) + 1
media_estudo = df[df["atividade"] == "Estudo"].groupby("semana")["minutos"].mean()





print("\n=-= TOTAL DE MINUTOS POR ATIVIDADE =-=")
print(total_por_atividade)

print("\n=-= TOTAL DE MINUTOS POR DIA =-=")
print(total_por_dia)

print("\n=-= ATIVIDADE MAIS REALIZADA =-=")
print(f"Atividade: {atividade_mais_tempo} — {minutos_atividade_mais} minutos")

print("\n=-= MÉDIA DE MINUTOS DE ESTUDO POR SEMANA =-=")
print(media_estudo)




print("\n=-=- RESUMO FINAL =-=-")
print("Periodo analisado:", df["semana"].nunique(), "semanas")
print("Atividade com maior carga de tempo:", atividade_mais_tempo)
print("Minutos totais registrados:", df["minutos"].sum())
print("Atividades registradas:", df["atividade"].nunique())
