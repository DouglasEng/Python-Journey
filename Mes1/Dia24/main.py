"""
=== Desafio do Dia 24 – Rastreador de Hábitos ===

Objetivo:
Criar um sistema simples para registrar e acompanhar hábitos diários.

Funcionalidades:
1. Registrar novo hábito
2. Listar hábitos do dia
3. Marcar hábito como concluído
4. Gerar relatório de desempenho
5. Salvar e carregar dados de habitos.txt
"""

import os

ARQUIVO = "habitos.txt"




def carregar_habitos():
    habitos = []
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                nome, status = linha.strip().split(" | ")
                habitos.append([nome, status])
    return habitos




def salvar_habitos(habitos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for nome, status in habitos:
            f.write(f"{nome} | {status}\n")




def registrar(habitos):
    nome = input("\nDigite o hábito a ser registrado: ").strip()
    habitos.append([nome, "não feito"])
    salvar_habitos(habitos)
    print("Hábito registrado!\n")


def listar(habitos):
    if not habitos:
        print("\nNenhum hábito registrado ainda.\n")
        return
    print("\n=-= Hábitos do Dia =-=")
    for i, (nome, status) in enumerate(habitos, start=1):
        print(f"{i}. {nome} → {status}")
    print()



def concluir(habitos):
    listar(habitos)
    if not habitos:
        return
    try:

        indice = int(input("Digite o número do hábito a concluir: "))
        if 1 <= indice <= len(habitos):
            habitos[indice-1][1] = "feito"
            salvar_habitos(habitos)
            print("Hábito concluído!\n")

        else:
            print("Número inválido!\n")

    except ValueError:
        print("Entrada inválida!\n")



def relatorio(habitos):
    if not habitos:
        print("\nNenhum hábito registrado para gerar relatório.\n")
        return
    feitos = sum(1 for _, status in habitos if status == "feito")
    nao_feitos = len(habitos) - feitos
    print("\n=-= Relatório do Dia =-=")
    print(f"Feitos: {feitos}")
    print(f"Não feitos: {nao_feitos}")
    print()




def menu():
    habitos = carregar_habitos()
    while True:
        print("=-=- Rastreador de Hábitos -=-=")
        print("(1) Registrar novo hábito")
        print("(2) Listar hábitos")
        print("(3) Marcar hábito como concluído")
        print("(4) Relatório do dia")
        print("(5) Sair")

        op = input("Escolha: ").strip()


        if op == "1":
            registrar(habitos)

        elif op == "2":
            listar(habitos)

        elif op == "3":
            concluir(habitos)

        elif op == "4":
            relatorio(habitos)

        elif op == "5":
            print("Até amanhã! Continue firme nos seus hábitos!")
            break
        
        else:
            print("Opção inválida!\n")





menu()
