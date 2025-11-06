"""
=== Desafio do Dia 65 — Mini Sistema de Tendências Numéricas ===


Descrição:
Crie um programa que leia uma sequência de números, armazene em
uma lista e apresente um pequeno relatório analítico com:
- Média, Mediana e Desvio Padrão
- O número mais comum (moda)
- A tendência da sequência (crescente, decrescente ou estável)
"""



import statistics
def analisar_lista(numeros):
    analise = {
        "média": statistics.mean(numeros),
        "mediana": statistics.median(numeros),
        "desvio_padrão": statistics.pstdev(numeros),
        "moda": statistics.mode(numeros)
    }
    if all(numeros[i] < numeros[i+1] for i in range(len(numeros)-1)):
        analise["tendência"] = "Crescente"
    elif all(numeros[i] > numeros[i+1] for i in range(len(numeros)-1)):
        analise["tendência"] = "Decrescente"
    else:
        analise["tendência"] = "Irregular/Estável"
    return analise


entrada = input("Digite uma sequência de numeros separados por espaço: ")
numeros = [float(n) for n in entrada.split()]
resultado = analisar_lista(numeros)



print("\Relatorio Analitico:")
for chave, valor in resultado.items():
    if isinstance(valor, float):
        print(f"{chave.title()}: {valor:.2f}")
    else:
        print(f"{chave.title()}: {valor}")
print("\nAnalise concluida com sucesso!")
