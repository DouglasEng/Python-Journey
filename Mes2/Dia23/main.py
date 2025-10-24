"""
=== Desafio do Dia 53 — Detector de Horários Produtivos ===
Tema: Análise de hábitos pessoais (programação + autoconhecimento)

Objetivo:
Criar um programa em Python que analise em quais horários do dia o usuário é mais produtivo.
O usuário informa em quais horas trabalhou em tarefas e a nota de produtividade (1 a 10).
O sistema grava as informações em um arquivo e, ao final, mostra o horário mais produtivo.

Desafios extras:
- Gravar e carregar os dados automaticamente de um arquivo ("produtividade.txt");
- Calcular o horário médio de maior produtividade;
- Exibir gráficos de produtividade (opcional para quem quiser usar matplotlib);
- Permitir limpar os dados com confirmação.
"""

import os
import statistics

ARQUIVO = "produtividade.txt"

def carregar_dados():
    if not os.path.exists(ARQUIVO):
        open(ARQUIVO, "w").close()
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        linhas = [linha.strip() for linha in f.readlines() if linha.strip()]
    registros = []
    for linha in linhas:
        hora, nota = linha.split(";")
        registros.append((int(hora), float(nota)))
    return registros



def salvar_dados(registros):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for hora, nota in registros:
            f.write(f"{hora};{nota}\n")



def registrar_produtividade(registros):
    try:
        hora = int(input("Digite a hora (0 a 23): "))
        if not 0 <= hora <= 23:
            raise ValueError
        nota = float(input("De 1 a 10, quão produtivo você foi? "))
        if not 1 <= nota <= 10:
            raise ValueError
        registros.append((hora, nota))
        salvar_dados(registros)
        print("Registro adicionado com sucesso!")
    except ValueError:
        print("Entrada invalida. Use números validos.")




def analisar_produtividade(registros):
    if not registros:
        print("Nenhum dado disponível ainda.")
        return

    horas = {}
    for hora, nota in registros:
        horas.setdefault(hora, []).append(nota)

    print("\n=-= Analise de Produtividade =-=")
    for hora, notas in sorted(horas.items()):
        media = sum(notas) / len(notas)
        print(f"{hora:02d}h → média {media:.1f}")

    melhor_hora = max(horas, key=lambda h: sum(horas[h]) / len(horas[h]))
    print(f"\nSeu horario mais produtivo costuma ser por volta das {melhor_hora:02d}h!")





def limpar_dados():
    confirmacao = input("Tem certeza que deseja apagar todos os dados? (s/n): ").lower()
    if confirmacao == "s":
        open(ARQUIVO, "w").close()
        print("Todos os dados foram apagados.")
    else:
        print("Operação cancelada.")




def main():
    registros = carregar_dados()
    while True:
        print("\n=-=- MENU =-=-")
        print("( 1 ) Registrar produtividade")
        print("( 2 ) Analisar horários")
        print("( 3 ) Limpar dados")
        print("( 4 ) Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_produtividade(registros)

        elif opcao == "2":
            analisar_produtividade(registros)


        elif opcao == "3":
            limpar_dados()
            registros = []


        elif opcao == "4":
            print("\nEncerrando o programa...")
            break


        else:
            print("Opção invalida, tente novamente.")






if __name__ == "__main__":
    main()
