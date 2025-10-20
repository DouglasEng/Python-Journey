"""
=== Desafio do Dia 49 – Simulador de Decisões Científicas ===

Objetivo:
Criar um programa que simule o processo de tomada de decisão em um experimento científico,
avaliando riscos, recursos e ética antes de aprovar a execução.  
A ideia é ajudar o usuário (pesquisador fictício) a refletir se o experimento é viável,
seguro e eticamente aceitável.

Funcionalidades:
1. Solicitar informações sobre um experimento (nome, objetivo, risco e impacto ético).
2. Atribuir pontuação de viabilidade com base nas respostas.
3. Gerar uma análise final classificando o experimento como:
   - "Aprovado"
   - "Necessita Revisão"
   - "Reprovado"
4. Registrar os resultados em um arquivo "decisoes_cientificas.txt".
"""







import os


ARQUIVO = "decisoes_cientificas.txt"

def avaliar_pergunta(pergunta, peso):
    while True:
        resp = input(pergunta + " (0-5): ").strip()
        if resp.isdigit() and 0 <= int(resp) <= 5:
            return int(resp) * peso
        print("Entrada invalida. Digite um número de 0 a 5.")






def classificar_resultado(pontuacao):
    if pontuacao >= 60:
        return "Aprovado"
    elif 35 <= pontuacao < 60:
        return "Necessita Revisão"
    else:
        return "Reprovado"
    



def salvar_resultado(nome, resultado, pontuacao):
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"Experimento: {nome}\nResultado: {resultado} ({pontuacao} pts)\n{'-'*40}\n")




def main():
    print("\n=-=- Simulador de Decisões Científicas =-=-\n")
    nome = input("Nome do experimento: ").strip()
    objetivo = input("Breve descrição do objetivo: ").strip()

    print("\nAvalie de 0 a 5 os seguintes aspectos:")
    risco = avaliar_pergunta("Nivel de risco envolvido", 3)
    impacto_positivo = avaliar_pergunta("Impacto positivo esperado para a sociedade", 4)
    impacto_ambiental = avaliar_pergunta("Cuidado com o impacto ambiental", 3)
    etica = avaliar_pergunta("Respeito a principios eticos e humanos", 5)
    viabilidade = avaliar_pergunta("Viabilidade e e economica", 4)

    pontuacao_total = impacto_positivo + impacto_ambiental + etica + viabilidade - risco
    resultado = classificar_resultado(pontuacao_total)

    print(f"\nAnalise do experimento '{nome}': {resultado}")
    print(f"Pontuação total: {pontuacao_total}\n")

    salvar = input("Deseja registrar essa decisão? (s/n): ").strip().lower()
    if salvar == "s":
        salvar_resultado(nome, resultado, pontuacao_total)
        print("Decisão registrada com sucesso!")






if __name__ == "__main__":
    main()
