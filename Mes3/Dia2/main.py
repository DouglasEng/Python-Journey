"""
=== Desafio do Dia 62 – Primeiros Passos com Pandas: Mini Analisador de Dados ===

Contexto:
Após analisarmos dados simulados manualmente no Dia 61, chegou a hora de introduzir
o uso da biblioteca 'pandas' — uma das bases da Análise e Ciência de Dados em Python.

Objetivo:
Criar um script curto que gera dados de treino simulados (como antes),
os converte em um DataFrame do pandas e realiza operações estatísticas e filtragens.

Conceitos trabalhados:
- Criação e manipulação de DataFrames
- Estatísticas descritivas básicas
- Filtragem e ordenação de dados
- Estrutura tabular e interpretação de resultados
"""



import pandas as pd
import numpy as np

np.random.seed(42)
n = 10
dados = {
    "Sessão": range(1, n + 1),
    "Volume": np.random.randint(8, 30, n),
    "Intensidade": np.round(np.random.uniform(6, 10, n), 1)
}
dados["Desempenho"] = np.round(dados["Volume"] * dados["Intensidade"] * np.random.uniform(0.8, 1.2, n), 2)
df = pd.DataFrame(dados)

print("=-= Análise Estatística Básica =-=")
print(df.describe())
media_desempenho = df["Desempenho"].mean()
acima_da_media = df[df["Desempenho"] > media_desempenho]

print("\n=-= Sessões acima da media de desempenho =-=")
print(acima_da_media[["Sessão", "Desempenho"]])
melhor = df.loc[df["Desempenho"].idxmax()]
pior = df.loc[df["Desempenho"].idxmin()]
print("\nMelhor Sessão:")
print(melhor)
print("\nPior Sessão:")
print(pior)
