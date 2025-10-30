"""
=== Desafio do Dia 53 — Analisador de Proporções Numéricas ===

O objetivo é explorar relações matemáticas entre números
e introduzir a ideia de razão, proporção e variação — conceitos
que são base de estatística e análise de dados.

Objetivo:
O programa deve receber uma lista de números e calcular:
 - a variação percentual entre cada elemento
 - a razão média entre valores consecutivos
 - detectar se há tendência de crescimento, queda ou oscilação

"""
valores = input("Digite os números separados por espaço: ")
numeros = [float(n) for n in valores.split()]

variacoes = []
for i in range(1, len(numeros)):
    variacao = ((numeros[i] - numeros[i-1]) / numeros[i-1]) * 100
    variacoes.append(variacao)

razoes = [numeros[i] / numeros[i-1] for i in range(1, len(numeros))]
razao_media = sum(razoes) / len(razoes)

if all(v > 0 for v in variacoes):
    tendencia = "CRESCENTE"
elif all(v < 0 for v in variacoes):
    tendencia = "DECRESCENTE"
else:
    tendencia = "OSCILANTE"

print("\nAnalise Matematica:")
print(f"Razão média: {razao_media:.3f}")
print(f"Variações percentuais: {[round(v, 2) for v in variacoes]}")
print(f"Tendência geral: {tendencia}")
