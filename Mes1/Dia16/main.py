"""
=== Desafio do Dia 17 – Mini Cadastro de Usuários com Arquivo ===

Objetivo:
Criar um programa que funcione como um pequeno sistema de cadastro de usuários,
permitindo adicionar, listar e buscar usuários, e salvando os dados em um arquivo
de texto para que não sejam perdidos entre execuções.

Funcionalidades:
- Adicionar usuário (nome, idade e email)
- Listar todos os usuários cadastrados
- Buscar usuários pelo nome
- Persistência de dados em arquivo 'usuarios.txt'

"""



import os

ARQUIVO_USUARIOS = os.path.join(os.path.dirname(__file__), "usuarios.txt")

def carregar_usuarios():
    if not os.path.exists(ARQUIVO_USUARIOS):
        return []
    usuarios = []
    with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
        for linha in f:
            partes = linha.strip().split(",")
            if len(partes) == 3:
                nome, idade, email = partes
                usuarios.append([nome, int(idade), email])
    return usuarios

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
        for u in usuarios:
            f.write(f"{u[0]},{u[1]},{u[2]}\n")









usuarios = carregar_usuarios()

while True:
    print("\n=-=- Menu do Cadastro =-=-")
    print("1 - Adicionar usuário")
    print("2 - Listar usuários")
    print("3 - Buscar usuário pelo nome")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome = input("Digite o nome: ").strip()
        idade = input("Digite a idade: ").strip()
        email = input("Digite o email: ").strip()

        if not idade.isdigit():
            print("Idade inválida! Usuário não adicionado.")
            continue

        usuarios.append([nome, int(idade), email])
        salvar_usuarios(usuarios)
        print(f"Usuário {nome} adicionado com sucesso!")



    elif opcao == "2":
        if not usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            print("\n=-=- Lista de Usuários =-=-")
            for i, u in enumerate(usuarios, start=1):
                print(f"{i}. Nome: {u[0]}, Idade: {u[1]}, Email: {u[2]}")



    elif opcao == "3":
        busca = input("Digite o nome a buscar: ").strip().lower()
        encontrados = []
        for u in usuarios:
            if busca in u[0].lower():
                encontrados.append(u)


        if not encontrados:
            print("Nenhum usuário encontrado.")
        else:
            print("\nUsuários encontrados:")
            for u in encontrados:
                print(f"Nome: {u[0]}, Idade: {u[1]}, Email: {u[2]}")



    elif opcao == "4":
        print("Saindo do sistema de cadastro...")
        break

    else:
        print("Opção inválida, tente novamente!")
