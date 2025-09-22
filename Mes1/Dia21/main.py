"""
=== Desafio do Dia 21 – Gerador de Nomes de Pets Lendários ===

Um programa que cria nomes únicos e mágicos para animais,
misturando partes aleatórias para formar combinações criativas.
"""

import random
import os

ARQUIVO = "pets.txt"

prefixos = ["Astro", "Luna", "Zyra", "Milo", "Koda", "Nebu", "Rexo"]
sufixos = ["dor", "nix", "fang", "paw", "tail", "fur", "claw"]




def gerar_nome(tipo):
    return random.choice(prefixos) + random.choice(sufixos) + f" o {tipo}"


def salvar(nome):
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(nome + "\n")




def ver_nomes():
    if not os.path.exists(ARQUIVO):
        print("\nNenhum nome gerado ainda.\n")
        return
    print("\n=-=- Pets Lendários Criados =-=-")
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        for linha in f:
            print(linha.strip())
    print()




def menu():
    while True:
        print("=-=- Gerador de Nomes de Pets Lendários =-=-")
        print("(1) Criar novo nome")
        print("(2) Ver todos os nomes criados")
        print("(3) Sair")
        opcao = input("Escolha: ").strip()


        if opcao == "1":
            tipo = input("Qual é o tipo do animal? ").strip().capitalize()
            nome = gerar_nome(tipo)
            print(f"\nNome criado: {nome}\n")
            salvar(nome)


        elif opcao == "2":
            ver_nomes()


        elif opcao == "3":
            print("Encerrando o gerador. Até a próxima aventura mágica!")
            break
        else:
            print("Opção inválida!\n")

menu()
