"""
=== Desafio do Dia 66 — Comparador de Conjuntos Numéricos ===
Tema: Análise e comparação de dados

Descrição:
Crie um programa que receba dois conjuntos de números
(ex: resultados de duas turmas, dois treinos, etc.)
e compare suas médias, informando:
  - Qual tem a média maior
  - A diferença entre elas
  - Se os conjuntos possuem tendência semelhante
"""





import statistics


def comparar_conjuntos(a, b):
    media_a = statistics.mean(a)
    media_b = statistics.mean(b)
    diferenca = abs(media_a - media_b)
    if media_a > media_b:
        melhor = "Conjunto A"
    elif media_b > media_a:
        melhor = "Conjunto B"
    else:
        melhor = "Empate"
    tendencia_a = "Crescente" if all(a[i] < a[i+1] for i in range(len(a)-1)) else "Irregular"
    tendencia_b = "Crescente" if all(b[i] < b[i+1] for i in range(len(b)-1)) else "Irregular"

    

    return {
        "Média A": round(media_a, 2),
        "Média B": round(media_b, 2),
        "Melhor Média": melhor,
        "Diferença": round(diferenca, 2),
        "Tendência A": tendencia_a,
        "Tendência B": tendencia_b
    }


print("Digite os numeros do conjunto A (separados por espaço):")
a = [float(x) for x in input().split()]
print("\nDigite os numeros do conjunto B (separados por espaço):")
b = [float(x) for x in input().split()]
resultado = comparar_conjuntos(a, b)
print("\nResultado comparativo:")
for chave, valor in resultado.items():
    print(f"{chave}: {valor}")

print("\nComparação finalizada com sucesso!")
