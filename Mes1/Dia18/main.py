"""
=== Desafio do Dia 18 – Tradutor Intergaláctico (Dupla Tradução) ===

Objetivo:
Criar um programa que traduza mensagens humanas para uma língua alienígena fictícia
e também consiga reverter essas mensagens alienígenas para "humano".

Regras:
-> Humano → Alien
1. Todas as vogais viram "ø".
2. Cada palavra é invertida.
3. Cada palavra recebe um sufixo aleatório (ex: -xar, -lok, -zor, -qul).

-> Alien → Humano
1. Remove o sufixo alienígena.
2. Inverte a palavra de volta.
3. Recupera a palavra original (usando o log salvo).

Além disso:
- O programa salva todas as traduções em um arquivo.
- O usuário pode traduzir, reverter, ver histórico ou sair.
"""

import os
import random

ARQUIVO = "alien_log.txt"
SUFIXOS = ["-xar", "-lok", "-zor", "-qul"]



def traduzir(frase):
    palavras = frase.lower().split()
    traduzidas = []

    for palavra in palavras:
        palavra_alien = "".join("ø" if c in "aeiou" else c for c in palavra)
        palavra_alien = palavra_alien[::-1]
        palavra_alien += random.choice(SUFIXOS)
        traduzidas.append(palavra_alien)

    return " ".join(traduzidas)


def reverter(frase_alien):
    palavras = frase_alien.split()
    revertidas = []

    for palavra in palavras:
        # remove sufixo
        for suf in SUFIXOS:
            if palavra.endswith(suf):
                palavra = palavra[: -len(suf)]
                break

        # inverte de volta
        palavra = palavra[::-1]

        # coloca 'a' como padrão para vogais alienígenas
        palavra = palavra.replace("ø", "a")
        revertidas.append(palavra)

    return " ".join(revertidas)


def salvar(frase, traducao, direcao):
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"[{direcao}] {frase} -> {traducao}\n")


def ver_historico():
    if not os.path.exists(ARQUIVO):
        print("\nNenhuma tradução feita ainda.\n")
        return
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        print("\n=-=- Histórico de Traduções -=-=\n")
        print(f.read())




def menu():
    while True:
        print("=-=- Tradutor Intergaláctico =-=-")
        print("1. Traduzir humano → alien")
        print("2. Traduzir alien → humano")
        print("3. Ver histórico")
        print("4. Sair")
        opcao = input("Escolha: ").strip()




        if opcao == "1":
            frase = input("\nDigite a frase em humano: ").strip()
            traducao = traduzir(frase)
            print(f"\nTradução alienígena: {traducao}\n")
            salvar(frase, traducao, "Humano→Alien")


        elif opcao == "2":
            frase = input("\nDigite a frase em alien: ").strip()
            traducao = reverter(frase)
            print(f"\nTradução humana (aproximada): {traducao}\n")
            salvar(frase, traducao, "Alien→Humano")


        elif opcao == "3":
            ver_historico()


        elif opcao == "4":
            print("Encerrando o tradutor. Até a próxima invasão!")
            break

        else:
            print("Opção inválida! Tente novamente.\n")



            

menu()
