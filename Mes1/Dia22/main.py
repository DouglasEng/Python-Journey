"""
=== Desafio do Dia 22 – Máquina do Tempo de Mensagens ===

Objetivo:
Criar uma máquina do tempo que permita ao usuário
enviar mensagens para o "futuro" (salvas em arquivo)
e ler mensagens do "passado" (já armazenadas em outro arquivo).
"""

import os

ARQ_FUTURO = "futuro.txt"
ARQ_PASSADO = "passado.txt"




def escrever_futuro():
    msg = input("\nDigite sua mensagem para o futuro: ").strip()
    with open(ARQ_FUTURO, "a", encoding="utf-8") as f:
        f.write(msg + "\n")
    print("Sua mensagem foi enviada para o futuro!\n")




def ler_passado():
    if not os.path.exists(ARQ_PASSADO):
        print("\nNenhuma mensagem do passado encontrada.\n")
        return
    print("\n==- Mensagens do Passado =-=")

    with open(ARQ_PASSADO, "r", encoding="utf-8") as f:
        for linha in f:
            print(linha.strip())
    print()




def menu():
    while True:
        print("=-=- Máquina do Tempo =-=-")
        print("1. Enviar mensagem para o futuro")
        print("2. Ler mensagens do passado")
        print("3. Sair")
        op = input("Escolha: ").strip()

        if op == "1":
            escrever_futuro()
        elif op == "2":
            ler_passado()
        elif op == "3":
            print("Encerrando a máquina do tempo.")
            break
        else:
            print("Opção inválida!\n")





menu()
