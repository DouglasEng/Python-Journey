"""
=== Desafio do Dia 38 – Rastreador de Hábitos com Pontuação ===

Objetivo:
Criar um sistema que ajuda o usuário a acompanhar seus hábitos diários e
ganhar pontos por consistência. O programa registra hábitos concluídos,
gera um histórico e mostra o desempenho total.

Descrição:
Cada hábito tem um nome e um número de pontos atribuídos.
Ao marcar um hábito como concluído, ele soma pontos ao total.
O sistema exibe o ranking dos hábitos mais feitos e a pontuação total acumulada.

Funcionalidades:
1. Registrar hábito concluído
2. Ver histórico completo
3. Analisar desempenho (ranking e pontos)
4. Sair
"""





import os
from datetime import datetime
from collections import defaultdict



ARQUIVO = "habitos.txt"



def registrar_habito():
    print("\n=-= Registrar Hábito Concluído =-=")
    habito = input("Nome do hábito (ex: Ler, Caminhar, Estudar...): ").strip().capitalize()
    pontos = input("Pontos ganhos (ex: 10): ").strip()

    if not pontos.isdigit():
        print("Valor inválido. Tente novamente.\n")
        return

    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"{data} | {habito} | {pontos}\n")

    print(f"Hábito '{habito}' registrado com sucesso! +{pontos} pontos.\n")



def ler_habitos():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        linhas = [linha.strip() for linha in f.readlines() if linha.strip()]
    return linhas



def ver_historico():
    habitos = ler_habitos()
    if not habitos:
        print("\nNenhum hábito registrado ainda.\n")
        return

    print("\n=-= Histórico de Hábitos =-=\n")
    for linha in habitos[-10:]: 
        print(linha)
    print()





def analisar_desempenho():


    habitos = ler_habitos()
    if not habitos:
        print("\nSem dados para analisar.\n")
        return
    total_pontos = 0
    ranking = defaultdict(int)
    for linha in habitos:
        try:
            _, nome, pontos = linha.split(" | ")
            pontos = int(pontos)
            ranking[nome] += pontos
            total_pontos += pontos
        except ValueError:
            continue
    print("\n=-= Análise de Desempenho =-=\n")
    print(f"Pontuação Total: {total_pontos} pontos\n")
    print("Hábitos mais praticados:")
    for nome, pts in sorted(ranking.items(), key=lambda x: x[1], reverse=True):
        print(f"- {nome}: {pts} pontos")
    print()





def menu():
    while True:
        print("=-=- Rastreador de Hábitos =-=-")
        print("( 1 ) Registrar Hábito Concluído")
        print("( 2 ) Ver Histórico")
        print("( 3 ) Analisar Desempenho")
        print("( 4 ) Sair")
        opcao = input("Escolha: ").strip()




        if opcao == "1":
            registrar_habito()

        elif opcao == "2":
            ver_historico()

        elif opcao == "3":
            analisar_desempenho()

        elif opcao == "4":
            print("Continue firme com seus hábitos!")
            break

        else:
            print("Opção inválida. Tente novamente.\n")







if __name__ == "__main__":
    menu()
