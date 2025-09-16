"""
=== Desafio do Dia 15 – Gerenciador de Tarefas ===

Objetivo:
Criar uma lista de tarefas simples com persistência em arquivo.

Regras:
1. O programa deve permitir ao usuário:
   - Adicionar tarefas
   - Listar tarefas
   - Remover tarefas concluídas
   - Sair
2. As tarefas devem ser salvas em "tarefas.txt".
3. Ao abrir o programa novamente, as tarefas já cadastradas devem aparecer.
4. O programa deve tratar erros, como tentar remover uma tarefa inexistente.
"""

import os

ARQUIVO_TAREFAS = os.path.join(os.path.dirname(__file__), "tarefas.txt")

def carregar_tarefas():
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f if linha.strip()]

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:
        for t in tarefas:
            f.write(t + "\n")








tarefas = carregar_tarefas()

while True:
    print("\n=-=- Menu =-=-")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        nova = input("Digite a nova tarefa: ")
        tarefas.append(nova)
        salvar_tarefas(tarefas)
        print("Tarefa adicionada!")



    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa encontrada.")
        else:
            print("\n=== Tarefas ===")
            for i, t in enumerate(tarefas, start=1):
                print(f"{i}. {t}")
            print("================")


    elif opcao == "3":
        if not tarefas:
            print("Nenhuma tarefa para remover.")
        else:
            try:
                num = int(input("Digite o número da tarefa para remover: "))
                removida = tarefas.pop(num - 1)
                salvar_tarefas(tarefas)
                print(f"Tarefa removida: {removida}")
            except (ValueError, IndexError):
                print("Número inválido!")




    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")
