"""
=== Desafio do Dia 26 – Calculadora de Gastos Diários com Registro ===

Objetivo:
Criar um programa que ajude o usuário a calcular quanto gastou em um dia,
informando valores de compras ao longo do dia e salvando os registros em um arquivo.

Funcionalidades:
1. O usuário digita os valores de cada gasto (até digitar 0 para encerrar).
2. O programa soma todos os valores.
3. Mostra o total gasto e a média por compra.
4. Registra todos os gastos em um arquivo de texto, junto com a data atual.
5. Permite consultar o histórico de gastos anteriores.
"""

import datetime
import os

ARQUIVO = "gastos.txt"




def registrar_gastos():
    gastos = []
    print("\n=-=- Calculadora de Gastos Diários -=-=")
    print("Digite seus gastos (0 para finalizar):")


    while True:
        try:
            valor = float(input("Gasto: R$ "))
            if valor == 0:
                break
            if valor < 0:
                print("Valor inválido. Digite apenas números positivos.")
                continue
            gastos.append(valor)


        except ValueError:
            print("Digite um valor numérico válido.")

    if gastos:
        total = sum(gastos)
        media = total / len(gastos)
        data = datetime.date.today().strftime("%d/%m/%Y")
        print(f"\nTotal gasto em {data}: R$ {total:.2f}")
        print(f"Média por compra: R$ {media:.2f}")

        with open(ARQUIVO, "a", encoding="utf-8") as f:
            f.write(f"{data} | Total: R$ {total:.2f} | Média: R$ {media:.2f} | Gastos: {gastos}\n")

    else:
        print("\nNenhum gasto registrado hoje.")




def ver_historico():
    if not os.path.exists(ARQUIVO):
        print("\nNenhum histórico encontrado ainda.")
        return
    print("\n=-=- Histórico de Gastos =-=-=")
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        for linha in f:
            print(linha.strip())




def menu():
    while True:
        print("\n=-=-= Menu =-=-=")
        print("(1) Registrar gastos do dia")
        print("(2) Ver histórico")
        print("(3) Sair")
        escolha = input("Escolha: ")



        if escolha == "1":
            registrar_gastos()

        elif escolha == "2":
            ver_historico()

        elif escolha == "3":
            print("Encerrando programa.")
            break

        else:
            print("Opção inválida, tente de novo.")





menu()
