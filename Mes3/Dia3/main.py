"""
=== Desafio do Dia 63 – Visualização Básica de Dados com Matplotlib ===

Contexto:
No desafio anterior, aprendemos a gerar e analisar dados com pandas.
Agora, vamos dar o próximo passo: visualizar esses dados de forma simples,
transformando números em gráficos que ajudam a interpretar tendências e padrões.

Objetivo:
Criar um script que gere os mesmos dados de treino (ou de desempenho físico)
e exiba gráficos básicos usando matplotlib.

Conceitos trabalhados:
- Importação e uso básico da biblioteca matplotlib
- Criação de gráficos de linha e barras
- Personalização de eixos e títulos
- Relação entre dados e visualização
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

plt.figure(figsize=(8, 4))
plt.plot(df["Sessão"], df["Desempenho"], marker='o', linestyle='-', label='Desempenho')
plt.title("Evolução do Desempenho nas Sessões de Treino")
plt.xlabel("Sessão")
plt.ylabel("Desempenho")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 4))
plt.bar(df["Sessão"], df["Volume"], alpha=0.7, label="Volume")
plt.bar(df["Sessão"], df["Intensidade"] * 3, alpha=0.7, label="Intensidade (x3)")
plt.title("Volume e Intensidade ao Longo das Sessões")
plt.xlabel("Sessão")
plt.ylabel("Valor Escalado")
plt.legend()
plt.show()
