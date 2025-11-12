""" 
=== Desafio do Dia 69 — Preditor Linear Simples ===


Descrição:
Desenvolva um programa que receba duas listas de valores numéricos
representando variáveis relacionadas (ex: horas de treino e peso levantado)
e gere uma linha de regressão linear simples que permita prever
novos valores da segunda variável com base na primeira.

Objetivos:
 - Reforçar o conceito de relação entre variáveis
 - Introduzir predição com regressão linear
 - Aplicar visualização gráfica e previsão numérica
"""





import numpy as np
import matplotlib.pyplot as plt




def coletar_dados():
    x = [float(i) for i in input("Digite os valores da variável X (ex: horas de treino): ").split()]
    y = [float(i) for i in input("Digite os valores da variável Y (ex: peso levantado): ").split()]

    if len(x) != len(y):
        print("As listas precisam ter o mesmo tamanho!")
        return None, None
    return np.array(x), np.array(y)



def calcular_regressao(x, y):
    m = np.cov(x, y, bias=True)[0, 1] / np.var(x)
    b = np.mean(y) - m * np.mean(x)
    return m, b



def prever(m, b, novo_x):
    return m * novo_x + b

def exibir_grafico(x, y, m, b):
    plt.scatter(x, y, label="Dados reais", color="orange")
    plt.plot(x, m * x + b, color="blue", label="Reta de Regressão")
    plt.title("Relação Linear entre Variáveis")
    plt.xlabel("Variável X")
    plt.ylabel("Variável Y")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()




print("=-=- Preditor linear simples =-=-")
x, y = coletar_dados()
if x is not None:
    m, b = calcular_regressao(x, y)
    print(f"\nEquação da reta: Y = {m:.2f}X + {b:.2f}")
    novo_x = float(input("\nDigite um novo valor de X para prever Y: "))
    previsao = prever(m, b, novo_x)
    print(f"Previsão: para X = {novo_x}, Y estimado = {previsao:.2f}\n")
    exibir_grafico(x, y, m, b)
else:
    print("Dados invalidos. Tente novamente.")
