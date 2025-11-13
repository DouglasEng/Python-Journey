"""
=== Desafio do Dia 70 — Avaliador de Precisão de Previsões ===

Descrição:
Dando sequência ao estudo de regressão linear, este desafio
consiste em avaliar a precisão das previsões feitas.

O programa deve calcular:
 - A equação da reta de regressão (Y = mX + b)
 - As previsões para cada X
 - O erro médio absoluto (MAE) entre valores reais e previstos

Objetivos:
 - Consolidar o entendimento de regressão linear
 - Introduzir métricas de avaliação de desempenho
 - Reforçar o uso de numpy e listas numéricas


"""





import numpy as np


def calcular_regressao(x, y):
    m = np.cov(x, y, bias=True)[0, 1] / np.var(x)
    b = np.mean(y) - m * np.mean(x)
    return m, b

def prever(m, b, x):
    return m * x + b



def erro_medio(y_real, y_previsto):
    return np.mean(np.abs(y_real - y_previsto))





print("=-=- Avaliador de precisão de previsões =-=-\n")
x = np.array([float(i) for i in input("Digite os valores de X: ").split()])
y = np.array([float(i) for i in input("Digite os valores reais de Y: ").split()])


if len(x) != len(y):
    print("\nErro: as listas precisam ter o mesmo tamanho.")
else:
    m, b = calcular_regressao(x, y)
    y_previsto = prever(m, b, x)
    mae = erro_medio(y, y_previsto)

    print(f"\nEquação da reta: Y = {m:.2f}X + {b:.2f}")
    print(f"Valores previstos: {np.round(y_previsto, 2)}")
    print(f"Erro médio absoluto (MAE): {mae:.4f}")


    if mae < 1:
        print("\nO modelo tem alta precisão.")
    elif mae < 3:
        print("\nO modelo tem precisão moderada.")
    else:
        print("\nO modelo apresenta erros altos — reveja os dados.")
