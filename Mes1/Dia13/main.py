"""
=== Desafio do Dia 13 – Analisador de Arquivo de Texto ===

Objetivo:
Ler um arquivo .txt e gerar estatísticas sobre o conteúdo do texto.

Regras:
1. O programa deve abrir e ler um arquivo chamado "texto.txt" (colocado na mesma pasta).
2. O texto deve ser processado para:
   - Número total de linhas
   - Número total de palavras
   - Número total de caracteres (sem contar espaços)
   - As 5 palavras mais frequentes
   - Quantas palavras únicas existem
   - Frequência das letras (a-z), ordenada da mais comum para a menos comum
3. Ignorar maiúsculas/minúsculas e remover pontuações (. , ! ?).

"""

import string

with open("texto.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

texto = conteudo.lower()
for p in string.punctuation:
    texto = texto.replace(p, "")

palavras = texto.split()





num_linhas = conteudo.count("\n") + 1
num_palavras = len(palavras)
num_caracteres = len(texto.replace(" ", ""))

contagem_palavras = {}
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1


top5 = sorted(contagem_palavras.items(), key=lambda x: x[1], reverse=True)[:5]
palavras_unicas = len([p for p, c in contagem_palavras.items() if c == 1])

contagem_letras = {}
for letra in texto.replace(" ", ""):
    if letra.isalpha():
        contagem_letras[letra] = contagem_letras.get(letra, 0) + 1

letras_ordenadas = sorted(contagem_letras.items(), key=lambda x: x[1], reverse=True)




print("\n-=-= Estatísticas do Arquivo -=-=")
print(f"Número de linhas: {num_linhas}")
print(f"Número total de palavras: {num_palavras}")
print(f"Número total de caracteres (sem espaços): {num_caracteres}")
print(f"Palavras únicas: {palavras_unicas}")

print("\nTop 5 palavras mais frequentes:")
for palavra, freq in top5:
    print(f"- {palavra}: {freq}x")

print("\nFrequência de letras (a-z):")
for letra, freq in letras_ordenadas:
    print(f"- {letra}: {freq}x")
