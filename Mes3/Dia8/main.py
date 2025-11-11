"""# 
=== Desafio do Dia 68 — Correlação entre Duas Variáveis ===

Descrição:
Desenvolva um programa que receba duas listas de valores numéricos
(por exemplo, horas de estudo e notas obtidas, ou peso e carga levantada)
e calcule o coeficiente de correlação entre elas, mostrando também
um gráfico de dispersão para visualização.

Objetivos:
 - Reforçar manipulação de listas numéricas
 - Introduzir o conceito de correlação entre variáveis
 - Utilizar visualização gráfica com matplotlib
"""



import numpy as np
import matplotlib.pyplot as plt

def coletar_dados():
    x = [float(i) for i in input("Digite os valores da primeira variavel (ex: horas de estudo): ").split()]
    y = [float(i) for i in input("Digite os valores da segunda variavel (ex: nota obtida): ").split()]
    if len(x) != len(y):
        print("As listas precisam ter o mesmo tamanho!")
        return None, None
    return x, y



def calcular_correlacao(x, y):
    return np.corrcoef(x, y)[0, 1]



def exibir_grafico(x, y, correlacao):
    plt.scatter(x, y, color='orange')
    plt.title(f"Correlação entre Variáveis (r = {correlacao:.2f})")
    plt.xlabel("Variavel X")
    plt.ylabel("Variavel Y")
    plt.grid(alpha=0.3)
    plt.show()




print("=== Analisador de Correlação ===")
x, y = coletar_dados()

if x and y:
    r = calcular_correlacao(x, y)
    print(f"\nCoeficiente de correlação: {r:.2f}")
    if r > 0.7:
        print("Forte correlação positiva.")
    elif r > 0.3:
        print("Correlação moderada positiva.")
    elif r > 0:
        print("Correlação fraca positiva.")
    elif r < -0.7:
        print("Forte correlação negativa.")
    elif r < -0.3:
        print("Correlação moderada negativa.")
    elif r < 0:
        print("Correlação fraca negativa.")
    else:
        print("Nenhuma correlação detectada.")
    exibir_grafico(x, y, r)


else:
    print("Erro: as listas não são compatíveis. Tente novamente.")
