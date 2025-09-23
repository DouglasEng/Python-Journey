"""
=== Desafio do Dia 23 – Biblioteca Cósmica ===

Objetivo:
Criar uma biblioteca de frases cósmicas, onde o usuário pode
registrar novos "conhecimentos universais", consultar frases
aleatórias ou listar todas.

Regras:
1. Registrar uma nova frase → salva em cosmos.txt
2. Consultar conhecimento cósmico aleatório → pega uma frase do arquivo
3. Listar todas as frases já salvas
"""

import os
import random

ARQUIVO = "cosmos.txt"

def adicionar_frase():
    frase = input("\nDigite o novo conhecimento cósmico: ").strip()
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(frase + "\n")
    print("Conhecimento registrado no universo!\n")


    

def consultar_frase():
    if not os.path.exists(ARQUIVO):
        print("\nNenhum conhecimento cósmico registrado ainda.\n")
        return
    
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        frases = f.readlines()

    if frases:
        print("\nSabedoria cósmica: ", random.choice(frases).strip(), "\n")
    else:
        print("\nAinda não há nada registrado no cosmos.\n")


def listar_frases():
    if not os.path.exists(ARQUIVO):
        print("\nNenhum conhecimento cósmico registrado ainda.\n")
        return
    print("\n=-= Todos os Conhecimentos Cósmicos =-=")
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        for i, linha in enumerate(f, start=1):
            print(f"{i}. {linha.strip()}")
    print()



def menu():
    while True:
        print("=-=- Biblioteca Cósmica =-=-")
        print("1. Registrar novo conhecimento")
        print("2. Consultar sabedoria cósmica aleatória")
        print("3. Listar todos os conhecimentos")
        print("4. Sair")
        op = input("Escolha: ").strip()

        if op == "1":
            adicionar_frase()


        elif op == "2":
            consultar_frase()


        elif op == "3":
            listar_frases()


        elif op == "4":
            print("Até a próxima viagem pelo cosmos!")
            break
        
        else:
            print("Opção inválida!\n")

menu()
