"""
=== Desafio do Dia 34 – Gerenciador de Sessões de Foco ===

Objetivo:
Criar um cronômetro de foco aprimorado (estilo Pomodoro),
que permite registrar múltiplas sessões, pausas e estatísticas simples.

Funcionalidades:
1. Definir tempo de foco e tempo de pausa.
2. Contar automaticamente o tempo de cada sessão.
3. Registrar todas as sessões concluídas em um arquivo "foco_log.txt".
4. Exibir estatísticas: total de minutos focados e quantidade de sessões concluídas.
5. Menu simples para iniciar nova sessão, ver histórico ou sair.
"""

import time
import os

ARQUIVO = "foco_log.txt"





def iniciar_sessao():
    try:
        foco = int(input("Duração do foco (minutos): ").strip())
        pausa = int(input("Duração da pausa (minutos): ").strip())
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.\n")
        return

    print(f"\nIniciando sessão de foco de {foco} minutos...\n")
    for restante in range(foco * 60, 0, -1):
        m, s = divmod(restante, 60)
        print(f"Tempo restante de foco: {m:02d}:{s:02d}", end="\r")
        time.sleep(1)




    print("\nFoco concluído! Hora da pausa!\n")
    for restante in range(pausa * 60, 0, -1):
        m, s = divmod(restante, 60)
        print(f"Tempo restante da pausa: {m:02d}:{s:02d}", end="\r")
        time.sleep(1)


    print("\nSessão completa! Pronto para a próxima?\n")
    registrar_sessao(foco)




def registrar_sessao(minutos):
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"{minutos}\n")





def ver_estatisticas():
    if not os.path.exists(ARQUIVO):
        print("\nNenhuma sessão registrada ainda.\n")
        return
    


    with open(ARQUIVO, "r", encoding="utf-8") as f:
        tempos = [int(linha.strip()) for linha in f if linha.strip().isdigit()]

    total_sessoes = len(tempos)
    total_minutos = sum(tempos)



    print(f"\nSessões concluídas: {total_sessoes}")
    print(f"Total de minutos focados: {total_minutos}\n")

def menu():
    while True:
        print("=-=- Gerenciador de Sessões de Foco =-=-")
        print("( 1 ) Iniciar nova sessão")
        print("( 2 ) Ver estatísticas")
        print("( 3 ) Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            iniciar_sessao()


        elif opcao == "2":
            ver_estatisticas()

        elif opcao == "3":
            print("Encerrando. Continue focado!")
            break

        else:
            print("Opção inválida.\n")





if __name__ == "__main__":
    menu()
