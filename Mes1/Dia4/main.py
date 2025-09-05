"""
=== Desafio do Dia 4 – Jogo da Forca ===

Objetivo:
Criar um jogo simples da forca em Python.

Regras:
1. O programa escolhe aleatoriamente uma palavra de uma lista pré-definida.
2. O jogador deve tentar adivinhar a palavra, chutando letras.
3. O jogador começa com 6 vidas.
4. Cada letra errada diminui 1 vida.
5. O jogo mostra as letras já acertadas e "_" para as ainda ocultas.
6. Se o jogador acertar todas as letras → Vitória.
7. Se perder todas as vidas → Derrota, mostrando a palavra correta.

"""


from random import randint

acervo = ["python", "banana", "computador", "teclado", 'programacao', "desenvolvimento", "jogo", 
          "forca", "desafio", "linguagem", "variavel", "função", "loop", "condicional", "lista", 
          "dicionario", "tupla", "conjunto", "string", "inteiro"]
vida = 6
palavra = acervo[randint(0, len(acervo) - 1)]
palavraDestrinchada = palavra.strip()

letras = []

while vida > 0:

    letra = input("\nDigite uma letra: ").lower()
    while letra in letras:
        letra = input("Letra já digitada, digite outra: ").lower()

    letras.append(letra)

    for contador in palavraDestrinchada:
        if contador in letras:
            print(contador, end=" ")
        else:
            print("_", end=" ")
            
    if letra not in palavraDestrinchada:
        vida -= 1
        print("\nLetra incorreta!")
    
    if all((letra in letras) for letra in palavraDestrinchada):
        print(f"\nParabéns! Você ganhou!")
        break

    print(f"\nVocê ainda tem {vida} vidas")
   
print(f"\nA palavra era {palavraDestrinchada}.")