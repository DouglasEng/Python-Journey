"""
=== Desafio do Dia 26 — Visualização de Hábitos de Estudo com Pandas + Matplotlib ===

Descrição:
Crie um DataFrame simulando horas estudadas ao longo de uma semana e analise os
dados com Pandas. Em seguida, produza visualizações simples com Matplotlib para
representar a evolução das horas estudadas e a eficiência diária.

Tarefas principais:
 - Criar DataFrame manualmente
 - Calcular estatísticas básicas
 - Criar coluna derivada de eficiência
 - Gráfico de linha (horas por dia)
 - Gráfico de barras (eficiência por dia)
"""





import pandas as pd
import matplotlib.pyplot as plt



df = pd.DataFrame({
    "dia": ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"],
    "horas": [2.5, 1.0, 3.2, 2.0, 4.1, 0.5, 0.0],
    "foco": [7, 4, 8, 6, 9, 2, 1]
})



media_horas = df["horas"].mean()
max_horas = df["horas"].max()
min_horas = df["horas"].min()



print("\n=-=- Resumo das horas de estudo =-=-")
print(f"Média: {media_horas:.2f}h")
print(f"Máximo: {max_horas}h ({df.loc[df['horas'].idxmax(), 'dia']})")
print(f"Mínimo: {min_horas}h ({df.loc[df['horas'].idxmin(), 'dia']})")


df["eficiencia"] = df["horas"] * (df["foco"] / 10)
print("\n=-= DataFrame atualizado =-=")
print(df)


plt.figure(figsize=(10, 4))
plt.plot(df["dia"], df["horas"], marker="o")
plt.title("Horas estudadas por dia")
plt.xlabel("Dia")
plt.ylabel("Horas")
plt.grid(True)
plt.tight_layout()
plt.show()



plt.figure(figsize=(10, 4))
plt.bar(df["dia"], df["eficiencia"])
plt.title("Eficiencia de estudo por dia")
plt.xlabel("Dia")
plt.ylabel("Eficiencia (horas * foco/10)")
plt.tight_layout()
plt.show()
