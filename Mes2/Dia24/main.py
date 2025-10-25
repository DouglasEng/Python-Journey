"""
=== Desafio do Dia 54 – Rastreador de Foco e Distração ===

Objetivo:
Criar um programa que ajuda o usuário a monitorar o tempo gasto focado em uma tarefa
versus o tempo gasto distraído. O sistema permite registrar sessões de trabalho
("foco") e pausas ("distração"), e ao final mostra um relatório com porcentagens.

Funcionalidades:
1. Iniciar ou encerrar uma sessão de foco
2. Iniciar ou encerrar uma sessão de distração
3. Exibir relatório de tempo total e porcentagem de foco
4. Limpar o histórico
"""





import os
import time
from datetime import datetime

ARQUIVO = "foco_diario.txt"




def registrar_evento(tipo):
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"{agora};{tipo}\n")
    print(f"{tipo.capitalize()} registrado às {agora}.")




def carregar_eventos():
    """le eventos registrados e retorna uma lista"""
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        linhas = [linha.strip() for linha in f.readlines() if linha.strip()]
    eventos = []
    for linha in linhas:
        data, tipo = linha.split(";")
        eventos.append((datetime.strptime(data, "%Y-%m-%d %H:%M:%S"), tipo))
    return eventos

def calcular_tempo(eventos):
    tempo_foco = 0
    tempo_distração = 0

    for i in range(0, len(eventos) - 1, 2):
        inicio, tipo_inicio = eventos[i]
        fim, tipo_fim = eventos[i + 1]
        duracao = (fim - inicio).total_seconds() / 60 
        if tipo_inicio == "foco":
            tempo_foco += duracao
        else:
            tempo_distração += duracao
    return tempo_foco, tempo_distração



def exibir_relatorio():
    eventos = carregar_eventos()
    if len(eventos) < 2:
        print("Nenhum dado suficiente para gerar relatório.")
        return

    tempo_foco, tempo_distração = calcular_tempo(eventos)
    total = tempo_foco + tempo_distração
    if total == 0:
        print("Nenhum tempo registrado ainda.")
        return
    porcentagem_foco = (tempo_foco / total) * 100
    print("\n=-= RELATORIO DE FOCO =-=")
    print(f"Tempo em foco: {tempo_foco:.1f} minutos")
    print(f"Tempo distraido: {tempo_distração:.1f} minutos")
    print(f"Percentual de foco: {porcentagem_foco:.1f}%")
    print("============================")





def limpar_dados():
    confirm = input("Tem certeza que deseja apagar o historico? (s/n): ").lower()
    if confirm == "s":
        open(ARQUIVO, "w").close()
        print("Historico apagado com sucesso.")
    else:
        print("Operação cancelada.")

def menu():
    while True:
        print("\n=-=- Rastreador de Foco =-=-")
        print("( 1 ) Iniciar sessão de foco")
        print("( 2 ) Iniciar sessão de distração")
        print("( 3 ) Ver relatório")
        print("( 4 ) Limpar histórico")
        print("( 5 ) Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_evento("foco")
            input("Pressione ENTER ao terminar a sessão...")
            registrar_evento("fim_foco")

        elif opcao == "2":
            registrar_evento("distração")
            input("Pressione ENTER ao terminar a pausa...")
            registrar_evento("fim_distração")

        elif opcao == "3":
            exibir_relatorio()

        elif opcao == "4":
            limpar_dados()

        elif opcao == "5":
            print("Encerrando programa...")



            break
        else:
            print("Opção invalida, tente novamente.")





            

if __name__ == "__main__":
    menu()
