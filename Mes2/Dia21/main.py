"""
=== Desafio do Dia 51 – Monitor de Foco e Produtividade ===

Objetivo:
Criar um programa que ajuda o usuário a gerenciar sessões de estudo ou trabalho,
medindo o tempo de foco e os intervalos de descanso — inspirado na técnica Pomodoro.

Contexto:
Manter o foco em longas sessões é um desafio real para quem programa, estuda ou trabalha
em frente ao computador. Este programa oferece um sistema simples de cronometragem
que registra os ciclos de foco e descanso, salvando o histórico localmente.

Funcionalidades:
1. O usuário define o tempo de foco e o tempo de descanso (em minutos)
2. O programa inicia uma contagem regressiva do tempo de foco
3. Quando o tempo termina, notifica e inicia automaticamente o período de descanso
4. Após cada ciclo, registra os dados (tempo e data) em um arquivo “foco_log.txt”
5. O usuário pode consultar o histórico de sessões anteriores
"""





import time
import os
from datetime import datetime





ARQUIVO = "foco_log.txt"

def contagem_regressiva(minutos, tipo):
    total_segundos = minutos * 60
    while total_segundos > 0:
        m, s = divmod(total_segundos, 60)
        print(f"\r{tipo} - Tempo restante: {m:02d}:{s:02d}", end="")
        time.sleep(1)
        total_segundos -= 1
    print(f"\nFim do período de {tipo.lower()}!\n")



def registrar_ciclo(foco, descanso):
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        agora = datetime.now().strftime("%d/%m/%Y %H:%M")
        f.write(f"{agora} - Foco: {foco}min / Descanso: {descanso}min\n")





def ver_historico():
    if not os.path.exists(ARQUIVO):
        print("\nNenhum histórico encontrado.\n")
        return
    print("\n=-= Histórico de Foco =-=")
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        print(f.read())





def iniciar_sessao():
    try:
        foco = int(input("Quantos minutos de foco? "))
        descanso = int(input("Quantos minutos de descanso? "))
    except ValueError:
        print("Entrada invalida. Use apenas numeros inteiros.\n")
        return

    print(f"\nIniciando foco de {foco} minutos...")
    contagem_regressiva(foco, "FOCO")

    print(f"Iniciando descanso de {descanso} minutos...")
    contagem_regressiva(descanso, "DESCANSO")

    registrar_ciclo(foco, descanso)
    print("Sessão registrada com sucesso!\n")





def menu():
    while True:
        print("=-=- Monitor de Foco e Produtividade =-=-")
        print("( 1 ) Iniciar nova sessão")
        print("( 2 ) Ver histórico de sessões")
        print("( 3 ) Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            iniciar_sessao()
        elif opcao == "2":
            ver_historico()
        elif opcao == "3":
            print("Encerrando o monitor. Bons estudos!")
            break
        else:
            print("Opção invalida.\n")




menu()
