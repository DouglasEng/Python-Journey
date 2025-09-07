"""
=== Desafio do Dia 6 – Caixa Eletrônico (Simples) ===

Objetivo:
Criar um programa que simule um caixa eletrônico com depósito, saque e consulta de saldo.

Regras:
1. O usuário começa com um saldo inicial (R$1000,00).
2. O programa deve exibir um menu com opções:
   - Depositar
   - Sacar
   - Consultar saldo
   - Sair
3. O saque só pode ser realizado se houver saldo suficiente.
4. O depósito deve ser um valor positivo.
5. O programa deve rodar em loop até o usuário escolher sair.

"""

import os

saldo = 1000.00


def consultar_saldo():
    print(f"\n💰 Saldo atual: R${saldo:.2f}")


def depositar():
    global saldo
    valor = float(input("Digite o valor para depósito: R$"))
    if valor > 0:
        saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido. Digite um valor positivo.")


def sacar():
    global saldo
    valor = float(input("Digite o valor para saque: R$"))
    if valor <= 0:
        print("Valor inválido. Digite um valor positivo.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso!")


while True:
    print("\n", "=-" * 20)
    print("=== Caixa Eletrônico ===")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    os.system('cls')  

    if opcao == "1":
        consultar_saldo()
    elif opcao == "2":
        depositar()
    elif opcao == "3":
        sacar()
    elif opcao == "4":
        print("\nObrigado por usar o Caixa Eletrônico.")
        break
    else:
        print("Opção inválida. Tente novamente.")
