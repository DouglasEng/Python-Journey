"""
=== Desafio do Dia 46 – Analisador de Experimentos Biológicos ===

Objetivo:
Criar um programa que leia dados experimentais de um arquivo (simulando medições biológicas)
e gere um relatório automático com estatísticas básicas e interpretações dos resultados.

Funcionalidades:
1. Ler dados de um arquivo .txt
2. Calcular estatísticas (média, máximo, mínimo)
3. Avaliar o comportamento do crescimento
4. Salvar relatório automático
5. Permitir novas análises
"""

import os
import statistics

def ler_dados(caminho):
    if not os.path.exists(caminho):
        print(f"Arquivo '{caminho}' não encontrado.\n")
        return None

    with open(caminho, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    dados = []
    for linha in linhas:
        try:
            valor = float(linha.strip())
            dados.append(valor)
        except ValueError:
            continue





    return dados

def interpretar_dados(dados):
    media = statistics.mean(dados)
    minimo = min(dados)
    maximo = max(dados)
    variacao = ((maximo - minimo) / media) * 100 if media != 0 else 0

    if media < 10:
        status = "Crescimento muito baixo (condições inadequadas)"
    elif 10 <= media < 50:
        status = "Crescimento estável e dentro do esperado"
    elif 50 <= media < 100:
        status = "Crescimento acelerado (possível mutação)"
    else:
        status = "Anomalia detectada (crescimento fora dos padrões)"

    return media, minimo, maximo, variacao, status






def gerar_relatorio(dados, caminho_relatorio):
    media, minimo, maximo, variacao, status = interpretar_dados(dados)
    conteudo = f"""
=-=- Relatorio de Analise Experimental =-=-
Total de medições: {len(dados)}
Média: {media:.2f}
Mínimo: {minimo:.2f}
Máximo: {maximo:.2f}
Variação: {variacao:.2f}%
Status: {status}
"""
    with open(caminho_relatorio, "w", encoding="utf-8") as f:
        f.write(conteudo.strip())

    print("\nAnalise concluída! Relatorio salvo em 'relatorio_experimento.txt'.\n")





def menu():
    while True:
        print("=-=- Analisador de Experimentos Biologicos =-=-")
        print("( 1 ) Analisar dados de experimento")
        print("( 2 ) Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            caminho = input("Digite o nome do arquivo (ex: dados_experimento.txt): ").strip()
            dados = ler_dados(caminho)
            if dados:
                gerar_relatorio(dados, "relatorio_experimento.txt")
        elif opcao == "2":
            print("Encerrando analise cientifica...")
            break
        else:
            print("Opção invalida. Tente novamente.\n")




menu()
