"""
=== Desafio do Dia 29 – Cofre de Senhas Simplificado ===

Objetivo:
Criar um programa que permita salvar e recuperar senhas de serviços de forma simples.
A ideia é simular um pequeno "cofre" local, útil para treinar manipulação de arquivos
e acesso seguro (mesmo que básico).

Funcionalidades:
1. Cadastrar um serviço e senha
2. Consultar senha de um serviço
3. Listar todos os serviços cadastrados
4. Encerrar

Observação:
- O objetivo é praticar leitura/escrita em arquivos e uso de dicionários.
"""

import os



ARQUIVO = "cofre.txt"





def carregar():
    dados = {}
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                servico, senha = linha.strip().split(" | ")
                dados[servico] = senha
    return dados



def salvar(dados):

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for servico, senha in dados.items():
            f.write(f"{servico} | {senha}\n")



def cadastrar(dados):
    servico = input("Nome do serviço: ").strip().lower()
    senha = input("Senha: ").strip()

    dados[servico] = senha
    salvar(dados)

    print("Salvo com sucesso!\n")



def consultar(dados):
    servico = input("Digite o serviço: ").strip().lower()
    if servico in dados:
        print(f"Senha de {servico}: {dados[servico]}\n")

    else:
        print("Serviço não encontrado.\n")



def listar(dados):
    if not dados:
        print("Nenhum serviço cadastrado.\n")

    else:
        print("\n=-= Serviços cadastrados =-=")
        for servico in dados:
            print(f"- {servico}")
        print()



def menu():
    dados = carregar()
    while True:
        print("=-=- Cofre de Senhas Simplificado =-=-")
        print("(1) Cadastrar nova senha")
        print("(2) Consultar senha")
        print("(3) Listar serviços")
        print("(4) Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            cadastrar(dados)

        elif opcao == "2":
            consultar(dados)

        elif opcao == "3":
            listar(dados)

        elif opcao == "4":
            print("Encerrando o cofre.")
            break

        else:
            print("Opção inválida.\n")





menu()
