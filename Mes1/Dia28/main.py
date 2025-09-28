"""
=== Desafio do Dia 28 – Planejador de Refeições Simples com Histórico ===

Objetivo:
Criar um programa que ajude a pessoa a organizar refeições com base nos ingredientes
que ela já tem em casa, evitando desperdício. Além disso, o programa deve salvar os
ingredientes cadastrados em um arquivo, permitindo reutilizar os dados em execuções futuras.

Funcionalidades:
1. Cadastrar ingredientes disponíveis
2. Salvar e carregar os ingredientes de um arquivo
3. Sugerir possíveis refeições simples baseadas em combinações pré-definidas
4. Consultar histórico de ingredientes cadastrados
5. Encerrar o programa
"""

import os

ARQUIVO = "ingredientes.txt"





receitas = {
    "PF clássico": {"arroz", "feijão", "ovo"},
    "Sanduíche": {"pão", "queijo"},
    "Macarronada": {"macarrão", "molho de tomate"},
    "Salada simples": {"alface", "tomate"},
    "Omelete": {"ovo", "queijo"},
    "Vitamina": {"leite", "banana"}
}

def carregar_ingredientes():
    if not os.path.exists(ARQUIVO):
        return set()
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return set(l.strip() for l in f if l.strip())
    


def salvar_ingredientes(ingredientes):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for item in sorted(ingredientes):

            f.write(item + "\n")



def cadastrar_ingredientes(ingredientes):
    print("\nDigite os ingredientes que você tem ('fim' para encerrar):")

    while True:
        item = input("Ingrediente: ").strip().lower()
        if item == "fim":
            break
        if item:
            ingredientes.add(item)

    salvar_ingredientes(ingredientes)




def sugerir_receitas(ingredientes):
    print("\n=-= Sugestões de Refeições ==-")
    encontrou = False

    for nome, itens in receitas.items():
        if itens.issubset(ingredientes):
            print(f"- {nome} (precisa de: {', '.join(itens)})")

            encontrou = True

    if not encontrou:

        print("Nenhuma refeição completa encontrada com os ingredientes disponíveis.")



def ver_historico(ingredientes):
    print("\n=-= Ingredientes cadastrados =-=")

    if not ingredientes:
        print("Nenhum ingrediente cadastrado ainda.")

    else:
        for item in sorted(ingredientes):
            print(f"- {item}")




def menu():
    ingredientes = carregar_ingredientes()
    while True:
        print("\n=-=- Planejador de Refeições Simples =-=-")
        print("(1) Cadastrar novos ingredientes")
        print("(2) Ver sugestões de refeições")
        print("(3) Ver histórico de ingredientes")
        print("(4) Sair")
        opcao = input("Escolha: ").strip()


        if opcao == "1":
            cadastrar_ingredientes(ingredientes)

        elif opcao == "2":
            sugerir_receitas(ingredientes)

        elif opcao == "3":
            ver_historico(ingredientes)

        elif opcao == "4":
            print("\nEncerrando programa. Bom apetite!")
            break

        else:
            print("Opção inválida! Tente novamente.")



            

menu()
