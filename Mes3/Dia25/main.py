"""
=== Desafio do Dia 25 — Mini Analisador de Desempenho Semanal (Pandas) ===

Descrição:
Crie um DataFrame simulando o desempenho de estudo ao longo de uma semana,
incluindo horas estudadas, matéria e nível de foco. Em seguida, aplique
operações básicas do Pandas (estatísticas, filtros, agrupamentos e coluna derivada).

Tarefas principais:
 - Criar DataFrame direto no código
 - Calcular métricas descritivas (média, máx, mín)
 - Filtrar dias acima/abaixo da média
 - Agrupar por matéria
 - Criar coluna derivada de produtividade
 - Exibir resumo final
"""




import pandas as pd



df = pd.DataFrame({
    "dia": ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"],
    "horas": [2.5, 1.0, 3.2, 2.0, 4.1, 0.5, 0],
    "materia": ["Python", "Pandas", "Python", "SQL", "Pandas", "Descanso", "Descanso"],
    "foco": [7, 4, 8, 6, 9, 2, 1]
})
media_horas = df["horas"].mean()
max_horas = df["horas"].max()
min_horas = df["horas"].min()


acima_media = df[df["horas"] > media_horas]
abaixo_media = df[df["horas"] < media_horas]
materias_freq = df["materia"].value_counts()
df["produtividade"] = df["horas"] * df["foco"]





print("\n=-=- Resumo geral =-=-")
print(f"Média de horas: {media_horas:.2f}")
print(f"Máx. horas estudadas: {max_horas}h")
print(f"Mín. horas estudadas: {min_horas}h")
print("\n=== Dias acima da média ===")
print(acima_media[["dia", "horas"]])
print("\n=-= Frequência por Matéria =-=")
print(materias_freq)
print("\n=-= DataFrame final com produtividade =-=")
print(df)
