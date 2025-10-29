"""
=== Desafio do dia 58 — Analisando Frequência de Palavras ===
Tema: Processamento de Texto e Contagem de Frequência

Funcionalidades:
O programa recebe um texto digitado pelo usuário e calcula
as palavras mais frequentes, ignorando maiúsculas e pontuações.

Conceitos trabalhados:
- Limpeza e padronização de dados textuais
- Uso de dicionários para contagem
- Ordenação de dados
"""

import string

texto = input("Digite um texto para analisar: ")

for p in string.punctuation:
    texto = texto.replace(p, "")
texto = texto.lower()

palavras = texto.split()

frequencia = {}
for palavra in palavras:
    frequencia[palavra] = frequencia.get(palavra, 0) + 1

frequencia_ordenada = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)

print("\nPalavras mais frequentes:")
for palavra, contagem in frequencia_ordenada[:5]:
    print(f"{palavra}: {contagem}x")
