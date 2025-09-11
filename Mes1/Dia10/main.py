"""
=== Desafio do Dia 10 – Top 3 Palavras Mais Frequentes ===

Objetivo:
Criar um programa que recebe um texto e retorna as 3 palavras mais usadas.

Regras:
1. O usuário digita um texto (uma ou mais frases).
2. O programa ignora maiúsculas/minúsculas.
3. Palavras são definidas como sequências de caracteres alfanuméricos (pontuação é ignorada).
4. Mostrar as 3 palavras mais frequentes, em ordem decrescente de frequência.
5. Se houver menos de 3 palavras diferentes, mostrar todas as existentes.

"""

import re

texto = input("Digite um texto: ")

palavras = re.findall(r"\b\w+\b", texto.lower())



if not palavras:
    print("\nNenhuma palavra encontrada no texto.")
else:
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1

    ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
    top3 = ordenado[:3]
    

    print("\nAs 3 palavras mais frequentes são:")
    for palavra, freq in top3:
        print(f"'{palavra}' apareceu {freq} vezes")
