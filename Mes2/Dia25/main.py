"""
=== Desafio do Dia 55 – Monitor Pessoal de Hábitos Ambientais ===

Objetivo:
Criar um programa que ajuda o usuário a monitorar seus hábitos diários relacionados
ao meio ambiente — como uso de transporte, energia e consumo de plástico — e calcular
um "índice pessoal de sustentabilidade" com base em suas respostas.

Funcionamento:
1. O usuário responde diariamente a um pequeno questionário sobre hábitos sustentáveis.
2. O sistema calcula um "índice verde" (0 a 100) com base nas respostas.
3. O resultado é armazenado em um arquivo `habitos_verdes.txt`.
4. O usuário pode ver seu histórico e média semanal.

Critérios do índice verde:
- Transporte: carro (0), transporte público (50), bicicleta/pé (100)
- Energia: sempre ligada (0), uso consciente (50), economia ativa (100)
- Plástico: muito (0), pouco (50), quase nada (100)
- Reciclagem: nunca (0), às vezes (50), sempre (100)
"""






import os

ARQUIVO = "habitos_verdes.txt"

def calcular_indice(respostas):
    pesos = {"transporte": 0.25, "energia": 0.25, "plastico": 0.25, "reciclagem": 0.25}
    soma = sum(respostas[k] * pesos[k] for k in respostas)
    return round(soma, 2)




def salvar_resultado(data, indice):
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"{data};{indice}\n")





def ver_historico():
    if not os.path.exists(ARQUIVO):
        print("\nNenhum dado registrado ainda.\n")
        return
    
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        linhas = [linha.strip() for linha in f if linha.strip()]
    
    total = 0
    for linha in linhas:
        data, indice = linha.split(";")
        print(f"{data} → Indice Verde: {indice}")
        total += float(indice)
    
    media = total / len(linhas)
    print(f"\nMedia geral: {media:.2f}\n")






def registrar_dia():
    from datetime import datetime
    data = datetime.now().strftime("%d/%m/%Y")
    print("\n=== Monitor de Habitos Sustentaveis ===")

    print("\nComo você se locomoveu hoje?")
    print("1. Carro particular\n2. Transporte público\n3. Bicicleta ou a pé")
    transporte = {"1": 0, "2": 50, "3": 100}[input("Escolha: ").strip()]

    print("\nComo foi seu uso de energia?")
    print("1. Desperdicei bastante\n2. Usei com cuidado\n3. Economizei ao máximo")
    energia = {"1": 0, "2": 50, "3": 100}[input("Escolha: ").strip()]

    print("\nQuanto plástico descartável você usou hoje?")
    print("1. Muito\n2. Pouco\n3. Quase nada")
    plastico = {"1": 0, "2": 50, "3": 100}[input("Escolha: ").strip()]

    print("\nVocê reciclou algo hoje?")
    print("1. Nunca\n2. Às vezes\n3. Sempre")
    reciclagem = {"1": 0, "2": 50, "3": 100}[input("Escolha: ").strip()]
    respostas = {
        "transporte": transporte,
        "energia": energia,
        "plastico": plastico,
        "reciclagem": reciclagem
    }
    indice = calcular_indice(respostas)
    salvar_resultado(data, indice)
    print(f"\nÍndice verde de hoje ({data}): {indice}\n")
    if indice >= 75:
        print("Excelente! Seu dia foi bem sustentável.")
    elif indice >= 50:
        print("Bom trabalho, mas há espaço para melhorar.")
    else:
        print("Que tal repensar algumas escolhas amanhã?")






def menu():
    while True:
        print("\n=-=- Monitor Pessoal de Hábitos Ambientais =-=-")
        print("1. Registrar hábitos de hoje")
        print("2. Ver histórico e média")
        print("3. Sair")
        escolha = input("Escolha: ").strip()

        if escolha == "1":
            registrar_dia()
        elif escolha == "2":
            ver_historico()
        elif escolha == "3":
            print("Encerrando o monitor verde...")
            break
        else:
            print("Opção invalida, tente novamente.")








if __name__ == "__main__":
    menu()
