"""
=== Desafio do Dia 48 – Consultor de Decisões Éticas ===

Objetivo:
Criar um programa que auxilie o usuário a refletir sobre uma decisão importante,
através de uma pequena análise lógica e ética.  
O programa propõe perguntas e, com base nas respostas, gera um parecer final
indicando se a decisão é razoável, impulsiva ou questionável.

Funcionalidades:
1. Fazer uma série de perguntas sobre a decisão do usuário.
2. Atribuir pontuações com base nas respostas.
3. Gerar uma análise final classificando o tipo de decisão.
4. (Extra) Permitir registrar a decisão em um arquivo “reflexoes.txt”.

"""

import os

ARQUIVO = "reflexoes.txt"




def perguntar(pergunta):
    while True:
        resposta = input(pergunta + " (s/n): ").strip().lower()
        if resposta == "s":
            return 2
        elif resposta == "n":
            return 0
        else:
            print("Resposta invalida. Digite apenas 's' ou 'n'.")



def analisar_decisao(pontos):
    if pontos >= 8:
        return "Decisão bem pensada. Você analisou lógica e eticamente a situação."
    elif 4 <= pontos < 8:
        return "Decisão parcialmente impulsiva. Vale refletir um pouco mais."
    else:
        return "Decisão questionável. Talvez seja melhor esperar e reconsiderar."
    

def salvar_reflexao(decisao, resultado):
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"Decisão: {decisao}\nResultado: {resultado}\n{'-'*40}\n")









def main():
    print("\n=-=- Consultor de Decisões Eticas =-=-")
    decisao = input("Sobre qual decisão você está refletindo? ").strip()

    print("\nResponda sinceramente as perguntas a seguir:\n")
    perguntas = [
        "Você avaliou possíveis consequências para outras pessoas?",
        "Você está tomando essa decisão por pressão emocional?",
        "Ela traz algum benefício coletivo, além do pessoal?",
        "Você está evitando agir por medo, e não por prudência?",
        "Você considerou alternativas antes de decidir?",
    ]
    pontos = 0
    for p in perguntas:
        pontos += perguntar(p)


    resultado = analisar_decisao(pontos)
    print(f"\nAnalise final: {resultado}")
    salvar = input("\nDeseja registrar essa reflexão? (s/n): ").strip().lower()
    if salvar == "s":
        salvar_reflexao(decisao, resultado)
        print("Reflexão registrada com sucesso!")








if __name__ == "__main__":
    main()
