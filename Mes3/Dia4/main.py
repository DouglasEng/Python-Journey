"""
=== Desafio do Dia 64 – Correlação entre Variáveis de Desempenho ===

Contexto:
Nos últimos desafios, aprendemos a gerar, analisar e visualizar dados com pandas e matplotlib.
Agora, vamos dar um passo além: investigar se há relação entre as variáveis que estamos estudando.

Objetivo:
Criar um programa que gere dados de treino e calcule a correlação entre Volume, Intensidade e Desempenho.
"""




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n = 10
dados = {
    "Sessão": range(1, n + 1),
    "Volume": np.random.randint(10, 30, n),
    "Intensidade": np.round(np.random.uniform(6, 10, n), 1)
}
dados["Desempenho"] = np.round(dados["Volume"] * dados["Intensidade"] * np.random.uniform(0.8, 1.2, n), 2)

df = pd.DataFrame(dados)
print("\n=-=- Dados Gerados =-=-")
print(df)

print("\n=-= Matriz de Correlação =-=")
correlacao = df[["Volume", "Intensidade", "Desempenho"]].corr()
print(correlacao)
plt.matshow(correlacao, cmap='coolwarm')
plt.colorbar(label="Coeficiente de correlação")
plt.xticks(range(len(correlacao.columns)), correlacao.columns, rotation=45)
plt.yticks(range(len(correlacao.columns)), correlacao.columns)
plt.title("Matriz de Correlação entre Variáveis", pad=20)
plt.show()
