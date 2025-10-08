"""
=== Desafio do Dia 37 – Analista Financeiro Pessoal ===

Objetivo:
Criar um sistema que registra as despesas e receitas do usuário, 
gera um resumo automático e identifica padrões financeiros, 
como os tipos de gastos mais frequentes e o saldo mensal acumulado.

Descrição:
O usuário pode registrar transações (entrada ou saída), visualizar todas,
analisar o total de gastos, ganhos e o saldo, além de descobrir onde gasta mais.

Funcionalidades:
1. Registrar transação
2. Ver todas as transações
3. Analisar finanças
4. Sair
"""




import os
from datetime import datetime
from collections import defaultdict

ARQUIVO = "financas.txt"

def registrar_transacao():
    print("\n=-= Registrar Transação =-=")
    tipo = input("Tipo (E = Entrada / S = Saída): ").strip().upper()
    categoria = input("Categoria (Ex: Alimentação, Transporte, Lazer...): ").capitalize()
    descricao = input("Descrição: ").strip()
    valor = float(input("Valor (ex: 150.75): ").replace(",", "."))
    data = datetime.now().strftime("%d/%m/%Y")

    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"{data} | {tipo} | {categoria} | {descricao} | {valor:.2f}\n")

    print("Transação registrada com sucesso!\n")

def ler_transacoes():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        linhas = [linha.strip() for linha in f.readlines() if linha.strip()]
    return linhas

def ver_transacoes():
    transacoes = ler_transacoes()
    if not transacoes:
        print("\nNenhuma transação encontrada.\n")
        return

    print("\n=-= Todas as Transações =-=\n")
    for t in transacoes:
        print(t)
    print()


def analisar_financas():
    transacoes = ler_transacoes()
    if not transacoes:
        print("\nNenhuma transação para analisar.\n")
        return
    total_entradas = 0
    total_saidas = 0
    por_categoria = defaultdict(float)

    for linha in transacoes:
        try:
            _, tipo, categoria, _, valor = linha.split(" | ")
            valor = float(valor)
            if tipo == "E":
                total_entradas += valor
            elif tipo == "S":
                total_saidas += valor
                por_categoria[categoria] += valor
        except ValueError:
            continue
    saldo = total_entradas - total_saidas

    print("\n=-= Análise Financeira =-=\n")
    print(f"Total de Entradas: R$ {total_entradas:.2f}")
    print(f"Total de Saídas:   R$ {total_saidas:.2f}")
    print(f"Saldo Atual:       R$ {saldo:.2f}\n")

    if por_categoria:
        print("Gastos por Categoria:")
        for cat, val in sorted(por_categoria.items(), key=lambda x: x[1], reverse=True):
            print(f"- {cat}: R$ {val:.2f}")
        print()





def menu():
    while True:
        print("-=-= Analista Financeiro Pessoal =-=-")
        print("( 1 ) Registrar Transação")
        print("( 2 ) Ver Todas as Transações")
        print("( 3 ) Analisar Finanças")
        print("( 4 ) Sair")
        opcao = input("Escolha: ").strip()



        if opcao == "1":
            registrar_transacao()

        elif opcao == "2":
            ver_transacoes()



        elif opcao == "3":
            analisar_financas()

        elif opcao == "4":
            print("Até logo! Continue cuidando bem das suas finanças")
            break


        else:
            print("Opção inválida, tente novamente.\n")






if __name__ == "__main__":
    menu()
