"""
=== Desafio do Dia 5 – Calculadora de IMC com Histórico ===

Objetivo:
Criar um programa que permita calcular o IMC (Índice de Massa Corporal) de várias pessoas,
manter um histórico de entradas, listar todas as pessoas cadastradas e filtrar por classificação.

Fórmula do IMC:
IMC = peso / (altura ** 2)

Classificação do IMC:
- IMC < 18.5 → Abaixo do peso
- 18.5 ≤ IMC < 25 → Normal
- 25 ≤ IMC < 30 → Sobrepeso
- IMC ≥ 30 → Obesidade

Funcionalidades:
1. Adicionar nova pessoa e calcular o IMC
2. Listar todas as pessoas cadastradas
3. Filtrar pessoas por classificação do IMC
4. Sair do programa

"""

pessoas = []

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

while True:
    print('\n', '=-'*20, '\n')
    pessoas.append([
            str(input('Nome: ')), 
            float(input('Peso(kg): ')), 
            float(input('Altura(m): '))
    ])
    
    pessoas[-1].append(pessoas[-1][1] / (pessoas[-1][2] ** 2))
    pessoas[-1].append(classificar_imc(pessoas[-1][3]))  

    cont = str(input('''\n1 - Listar\n2 - Sair\nEscolha: '''))

    if cont == '1':
        print(f"\n{'Nome':<15} {'Peso':<10} {'Altura':<8} {'IMC':<8}{'Classificação'}")
        print('-'*50)

        for p in pessoas:
            print(f"{p[0]:<15} {p[1]:<10} {p[2]:<8} {p[3]:<8.2f} {p[4]}")

    elif cont == '2':
        break

print(f"\n{'Nome':<15} {'Peso':<10} {'Altura':<8} {'IMC':<8} {'Classificação'}")

print('-'*50)


for p in pessoas:
    print(f"{p[0]:<15} {p[1]:<10} {p[2]:<8} {p[3]:<8.2f} {p[4]}")
