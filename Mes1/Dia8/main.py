"""
=== Desafio do Dia 8 – Sistema de Cadastro e Estatísticas de Alunos ===

Objetivo:
Criar um programa que permita cadastrar vários alunos, armazenando:
- Nome
- Idade
- Nota final

E gerar estatísticas e relatórios com base nos dados cadastrados.

Funcionalidades:
1. Adicionar novos alunos
2. Listar todos os alunos cadastrados
3. Mostrar a média das notas
4. Mostrar o aluno com maior e menor nota
5. Contar quantos alunos foram aprovados (nota >= 7) e reprovados (nota < 7)
6. Sair do programa

"""

alunos = []


def adicionar_aluno():
    nome = input("Nome do aluno: ").strip().title()

    while True:
        try:
            idade = int(input("Idade: "))
            if idade <= 0:
                print("Idade deve ser positiva.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro para idade.")

    while True:
        try:
            nota = float(input("Nota final (0-10): "))
            if 0 <= nota <= 10:
                break
            else:
                print("Nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número válido para nota.")

    alunos.append({"nome": nome, "idade": idade, "nota": nota})
    print(f"Aluno {nome} adicionado com sucesso!\n")



def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return
    print("\n=== Lista de Alunos ===")
    for idx, aluno in enumerate(alunos, start=1):
        print(f"{idx}. {aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']:.2f}")
    print()


def estatisticas():
    if not alunos:
        print("Nenhum aluno cadastrado para gerar estatísticas.\n")
        return
    
    notas = [aluno["nota"] for aluno in alunos]
    media = sum(notas) / len(notas)
    maior = max(alunos, key=lambda x: x["nota"])
    menor = min(alunos, key=lambda x: x["nota"])
    aprovados = len([aluno for aluno in alunos if aluno["nota"] >= 7])
    reprovados = len([aluno for aluno in alunos if aluno["nota"] < 7])

    print("\n=== Estatísticas ===")
    print(f"Média das notas: {media:.2f}")
    print(f"Maior nota: {maior['nota']:.2f} ({maior['nome']})")
    print(f"Menor nota: {menor['nota']:.2f} ({menor['nome']})")
    print(f"Aprovados: {aprovados}")
    print(f"Reprovados: {reprovados}\n")







while True:
    print("=== Sistema de Cadastro de Alunos ===")
    print("1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Estatísticas")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        adicionar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        estatisticas()
    elif opcao == "4":
        print("Obrigado! Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
