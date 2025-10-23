"""
=== Desafio do Dia 52 — Criptografia de César Avançada ===

Objetivo:
Implementar uma cifra de César que permita criptografar ou descriptografar textos
com deslocamento definido pelo usuário, preservando letras maiúsculas/minúsculas
e ignorando caracteres especiais. O programa também deve exibir o tempo de execução.
"""

import time

def cifra_cesar(texto, deslocamento, modo):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            if modo == "criptografar":
                resultado += chr((ord(char) - base + deslocamento) % 26 + base)
            elif modo == "descriptografar":
                resultado += chr((ord(char) - base - deslocamento) % 26 + base)
        else:
            resultado += char
    return resultado



def main():
    print("=-=- Cifra de Cesar Avançada =-=-")
    texto = input("Digite o texto: ")
    deslocamento = int(input("Digite o numero de casas para deslocamento: "))
    modo = input("Deseja criptografar ou descriptografar? ").lower()
    inicio = time.time()
    resultado = cifra_cesar(texto, deslocamento, modo)
    fim = time.time()


    print("\nResultado:", resultado)
    print(f"Tempo de execução: {fim - inicio:.6f} segundos")





if __name__ == "__main__":
    main()
