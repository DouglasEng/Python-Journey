"""
=== Desafio do Dia 27 – Conversor Inteligente de Unidades ===

Objetivo:
Criar um programa que ajude o usuário a converter diferentes unidades do dia a dia.
O sistema deve permitir que o usuário escolha qual tipo de conversão deseja realizar
e aplicar a fórmula correta automaticamente.

Funcionalidades:
1. Converter temperaturas (Celsius ↔ Fahrenheit)
2. Converter distâncias (Km ↔ Milhas)
3. Converter pesos (Kg ↔ Libras)
4. Sair do programa

Detalhes técnicos:
- Usar funções para cada tipo de conversão
- Utilizar dicionário para mapear opções do menu
- Permitir repetições até o usuário decidir sair
- Garantir que a entrada seja válida (tratamento simples de erros)
"""


def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def km_para_milhas(km):
    return km * 0.621371


def milhas_para_km(milhas):
    return milhas / 0.621371


def kg_para_libras(kg):
    return kg * 2.20462


def libras_para_kg(lb):
    return lb / 2.20462


opcoes = {

    "1": "Celsius → Fahrenheit",
    "2": "Fahrenheit → Celsius",
    "3": "Km → Milhas",
    "4": "Milhas → Km",
    "5": "Kg → Libras",
    "6": "Libras → Kg",
    "7": "Sair"
}

while True:
    print("\n=-= Conversor de Unidades =-=")

    for chave, valor in opcoes.items():
        print(f"{chave}. {valor}")
    
    escolha = input("Escolha uma opção: ")

    
    if escolha == "7":
        print("Saindo... até a próxima!")
        break
    
    if escolha not in opcoes:
        print("Opção inválida. Tente novamente.")
        continue
    
    try:
        valor = float(input("Digite o valor a ser convertido: "))
    except ValueError:
        print("Entrada inválida! Digite um número.")
        continue

    
    if escolha == "1":
        print(f"{valor}°C = {celsius_para_fahrenheit(valor):.2f}°F")

    elif escolha == "2":
        print(f"{valor}°F = {fahrenheit_para_celsius(valor):.2f}°C")

    elif escolha == "3":
        print(f"{valor} Km = {km_para_milhas(valor):.2f} Milhas")

    elif escolha == "4":
        print(f"{valor} Milhas = {milhas_para_km(valor):.2f} Km")

    elif escolha == "5":
        print(f"{valor} Kg = {kg_para_libras(valor):.2f} Libras")

    elif escolha == "6":
        print(f"{valor} Libras = {libras_para_kg(valor):.2f} Kg")
    
