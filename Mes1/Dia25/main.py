"""
=== Desafio do Dia 26 – Enciclopédia Animal Expandida ===

Objetivo:
Criar um programa que funcione como uma pequena enciclopédia de animais, 
permitindo registrar novas curiosidades, consultar informações já existentes 
e manter um histórico persistente em arquivo de texto.

Regras:
- Todas as informações são salvas no arquivo "animais.txt".
- Ao iniciar, o programa carrega os dados já existentes.
- Caso um animal não esteja cadastrado, o usuário pode adicioná-lo.

Funcionalidades:
1. Consultar um animal específico e visualizar sua curiosidade
2. Adicionar um novo animal com sua curiosidade
3. Listar todos os animais cadastrados até o momento
4. Encerrar o programa
"""


import os

ARQUIVO = "animais.txt"



def carregar_animais():
    animais = {}
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                if ":" in linha:
                    animal, curiosidade = linha.strip().split(":", 1)
                    animais[animal.lower()] = curiosidade
    return animais



def salvar_animais(animais):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for animal, curiosidade in animais.items():
            f.write(f"{animal}:{curiosidade}\n")




def menu():
    animais = carregar_animais()

    while True:
        print("\n=== Enciclopédia Animal Expandida ===")
        print("1. Consultar animal")
        print("2. Adicionar novo animal")
        print("3. Listar todos os animais")
        print("4. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            animal = input("Digite o nome do animal: ").lower().strip()

            if animal in animais:
                print(f"Curiosidade: {animais[animal]}")
            else:
                print("Ainda não temos informações sobre esse animal.")




        elif opcao == "2":
            animal = input("Digite o nome do animal: ").lower().strip()

            if animal in animais:
                print("Esse animal já está registrado.")

            else:
                curiosidade = input("Digite uma curiosidade sobre ele: ").strip()

                animais[animal] = curiosidade
                salvar_animais(animais)
                print("Novo animal registrado com sucesso!")


        elif opcao == "3":
            if animais:
                print("=-= Animais Registrados =-=")

                for a in animais:
                    print(f"- {a.capitalize()}")

            else:
                print("Nenhum animal registrado ainda.")



        elif opcao == "4":
            print("Encerrando a Enciclopédia Animal Expandida...")
            break


        else:
            print("Opção inválida. Tente novamente.")






menu()
