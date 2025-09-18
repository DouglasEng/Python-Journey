"""
=== Desafio do Dia 17 – Diário Secreto de Aventuras ===

Objetivo:
Construir um diário digital onde o usuário pode registrar suas aventuras,
consultar as já registradas e buscar por título. Todas as informações ficam
armazenadas em um arquivo de texto dentro da mesma pasta do programa,
permitindo que o conteúdo seja mantido mesmo após fechar a aplicação.

Regras:
1. O usuário poderá adicionar novas aventuras, informando título, data e descrição.
2. Deve ser possível listar todas as aventuras salvas de forma organizada.
3. Também é deverá ser possível buscar aventuras pelo título ou parte dele.
4. O programa deve continuar em execução até o usuário escolher a opção de sair.

"""


import os

ARQUIVO = "diario.txt"

def carregar_aventuras():
    aventuras = []

    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                partes = linha.strip().split(" | ")
                if len(partes) == 3:
                    aventuras.append(partes)

    return aventuras



def salvar_aventuras(aventuras):

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for aventura in aventuras:
            f.write(" | ".join(aventura) + "\n")



def registrar(aventuras):
    titulo = input("Digite o título da aventura: ").strip()
    data = input("Digite a data (ex: 17/09/2025): ").strip()
    desc = input("Conte como foi: ").strip()
    aventuras.append([titulo, data, desc])
    salvar_aventuras(aventuras)
    print("Aventura registrada!\n")



def listar(aventuras):
    if not aventuras:
        print("Nenhuma aventura encontrada ainda.\n")
        return
    
    print("\n=-=- Suas Aventuras =-=-")

    for i, (titulo, data, desc) in enumerate(aventuras, start=1):
        print(f"{i}. {titulo} ({data})")
        print(f"   {desc}\n")



def buscar(aventuras):
    termo = input("Digite o título ou parte dele: ").strip().lower()
    achou = False

    for titulo, data, desc in aventuras:
        if termo in titulo.lower():
            print(f"\nEncontrado: {titulo} ({data})")
            print(f"   {desc}\n")
            achou = True

    if not achou:
        print("Nenhuma aventura encontrada com esse título.\n")



def menu():
    aventuras = carregar_aventuras()

    while True:
        print("Diário Secreto de Aventuras")
        print("1. Registrar nova aventura")
        print("2. Listar todas as aventuras")
        print("3. Buscar aventura pelo título")
        print("4. Sair")
        escolha = input("Escolha: ").strip()

        if escolha == "1":
            registrar(aventuras)
        elif escolha == "2":
            listar(aventuras)
        elif escolha == "3":
            buscar(aventuras)
        elif escolha == "4":
            print("Até logo, aventureiro!")
            break
        else:
            print("Opção inválida, tente de novo.\n")









menu()
