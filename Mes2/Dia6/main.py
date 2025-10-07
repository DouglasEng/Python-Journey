"""
=== Desafio do Dia 36 – Diário de Humor Inteligente ===

Objetivo:
Criar um programa que registre o humor diário do usuário e forneça
um resumo emocional com base nas entradas anteriores.

Descrição:
O usuário informa como está se sentindo (ex: feliz, cansado, ansioso, animado),
e o programa salva a data, o humor e um breve comentário opcional.
Ao longo do tempo, o sistema analisa as entradas e mostra tendências emocionais,
como qual humor é mais frequente e em quais dias da semana o usuário tende a se sentir melhor.

Funcionalidades:
1. Registrar humor do dia
2. Ver histórico completo
3. Analisar tendências de humor
4. Sair do programa

"""




import os
from datetime import datetime
from collections import Counter

ARQUIVO = "humor_log.txt"

def registrar_humor():
    data = datetime.now().strftime("%d/%m/%Y (%A)")
    humor = input("Como você está se sentindo hoje? ").strip().capitalize()
    comentario = input("Quer deixar um comentário opcional? (ou pressione Enter) ").strip()

    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"{data} | {humor} | {comentario}\n")

    print("\nHumor registrado!\n")



def ler_historico():
    if not os.path.exists(ARQUIVO):
        print("\nNenhum registro encontrado.\n")
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        linhas = [linha.strip() for linha in f.readlines() if linha.strip()]
    return linhas



def ver_historico():
    registros = ler_historico()
    if not registros:
        return
    print("\n=-= Histórico de Humor =-=\n")
    for linha in registros:
        print(linha)
    print()





def analisar_tendencias():
    registros = ler_historico()
    if not registros:
        return
    humores = []
    dias_semana = []

    for linha in registros:
        try:
            data_str, humor, *_ = linha.split(" | ")
            dia_semana = data_str.split("(")[-1].replace(")", "")
            dias_semana.append(dia_semana)
            humores.append(humor)
        except ValueError:
            continue
    print("\n=-= Análise Emocional =-=\n")

    if humores:
        mais_comum = Counter(humores).most_common(1)[0]
        print(f"Humor mais frequente: {mais_comum[0]} ({mais_comum[1]} vezes)")


    if dias_semana:
        dia_feliz = Counter(dias_semana).most_common(1)[0]
        print(f"Dia da semana mais registrado: {dia_feliz[0]}")

    print()



def menu():
    while True:
        print("=-=- Diário de Humor Inteligente =-=-")
        print("( 1 ) Registrar humor de hoje")
        print("( 2 ) Ver histórico completo")
        print("( 3 ) Analisar tendências de humor")
        print("( 4 ) Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            registrar_humor()

    
        elif opcao == "2":
            ver_historico()
        elif opcao == "3":
            analisar_tendencias()

        elif opcao == "4":
            print("Até amanhã! Cuide bem do seu humor :)")
            break

        else:
            print("Opção inválida, tente novamente.\n")





if __name__ == "__main__":
    menu()
