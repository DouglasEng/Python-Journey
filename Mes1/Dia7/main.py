"""
=== Desafio do Dia 7 – Calculadora Completa de Operações ===

Objetivo:
Criar um programa que leia um número inteiro e exiba várias operações matemáticas:
1. Dobro, triplo e raiz quadrada
2. Fatorial
3. Verificação se é primo ou não
4. Contagem regressiva até zero

Regras:
- O número deve ser inteiro e positivo
- Cada operação deve ser realizada dentro de uma função
- Saída organizada e legível

"""

import math
import time

def operacoes_basicas(n):
    dobro = n * 2
    triplo = n * 3
    raiz = n ** 0.5
    return dobro, triplo, raiz

def fatorial(n):
    return math.factorial(n)

def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def contagem_regressiva(n):
    print(f"\nContagem regressiva de {n} até 0:")
    for i in range(n, -1, -1):
        print(i, end=' ', flush=True)
        time.sleep(0.3)
    print()





while True:
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero >= 0:
            break
        else:
            print("O número deve ser positivo.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")


dobro, triplo, raiz = operacoes_basicas(numero)
fato = fatorial(numero)
primo = primo(numero)

print("\n=== Resultados ===")
print(f"Número digitado: {numero}")
print(f"Dobro: {dobro}")
print(f"Triplo: {triplo}")
print(f"Raiz quadrada: {raiz:.2f}")
print(f"Fatorial: {fato}")
print(f"É primo? {'Sim' if primo else 'Não'}")

contagem_regressiva(numero)
