"""
=== Desafio do Dia 84 — Mini-Análise da Rotina Gamer com Pandas ===

Descrição:
Este desafio utiliza apenas dados criados no próprio código para simular a rotina
de horas jogadas durante a semana. O objetivo é praticar operações básicas do Pandas:
criação de DataFrame, agregações, filtros e manipulação de colunas.

Tarefas principais:
 - Criar um DataFrame manual com dias da semana, horas jogadas, gênero do jogo e humor.
 - Calcular estatísticas simples:
       • Total de horas jogadas na semana
       • Dia com mais horas de gameplay
       • Gênero mais jogado
       • Média do humor por gênero de jogo
 - Filtrar dias com mais de 3h jogadas
 - Criar uma coluna indicando dias “produtivos” (menos de 2h de jogo)
"""




import pandas as pd


data = {
    "day": ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"],
    "hours_played": [1.5, 3, 2, 4, 5, 6, 2.5],
    "game_genre": ["RPG", "FPS", "RPG", "Corrida", "FPS", "RPG", "MOBA"],
    "mood": [7, 6, 8, 7, 9, 10, 6]  # humor de 0 a 10
}
df = pd.DataFrame(data)

total_hours = df["hours_played"].sum()
best_day = df.loc[df["hours_played"].idxmax(), "day"]
most_played_genre = df["game_genre"].mode()[0]
avg_mood_by_genre = df.groupby("game_genre")["mood"].mean()
heavy_days = df[df["hours_played"] > 3]
df["productive_day"] = df["hours_played"] < 2






print("=-=- ANÁLISE ===")
print(df)
print("\nTotal de horas jogadas na semana:", total_hours)
print("Dia com mais jogo:", best_day)
print("Gênero mais jogado:", most_played_genre)
print("\nMédia do humor por gênero:")
print(avg_mood_by_genre)
print("\nDias com mais de 3h de jogo:")
print(heavy_days)
