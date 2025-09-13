"""
=== Desafio do Dia 12 – Analisador de Texto ===

Objetivo:
Criar um programa que receba um texto digitado pelo usuário e gere estatísticas sobre ele.

Regras:
1. O usuário digita um texto (frase ou parágrafo).
2. O programa deve calcular e exibir:
   - Número total de palavras
   - Número de caracteres (sem contar espaços)
   - As 3 palavras mais frequentes e suas contagens
   - Quantas palavras únicas existem no texto
   - Frequência de cada letra (a-z), ordenada da mais comum para a menos comum
3. Ignorar maiúsculas/minúsculas na contagem (case insensitive).
4. Descartar pontuações simples (. , ! ?).

"""




import string

texto = input("Digite um texto para análise:\n")

texto_limpo = texto.lower()
for p in string.punctuation:
    texto_limpo = texto_limpo.replace(p, "")

palavras = texto_limpo.split()

num_palavras = len(palavras)
num_caracteres = len(texto_limpo.replace(" ", ""))

contagem_palavras = {}
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

top3 = sorted(contagem_palavras.items(), key=lambda x: x[1], reverse=True)[:3]

palavras_unicas = len([p for p, c in contagem_palavras.items() if c == 1])

contagem_letras = {}
for letra in texto_limpo.replace(" ", ""):
    if letra.isalpha():
        contagem_letras[letra] = contagem_letras.get(letra, 0) + 1

letras_ordenadas = sorted(contagem_letras.items(), key=lambda x: x[1], reverse=True)





print("\n=-=- Estatísticas do Texto -=-=")
print(f"Número total de palavras: {num_palavras}")
print(f"Número total de caracteres (sem espaços): {num_caracteres}")
print(f"Palavras únicas: {palavras_unicas}")

print("\nTop 3 palavras mais frequentes:")
for palavra, freq in top3:
    print(f"- {palavra}: {freq}x")

print("\nFrequência de letras (a-z):")
for letra, freq in letras_ordenadas:
    print(f"- {letra}: {freq}x")
