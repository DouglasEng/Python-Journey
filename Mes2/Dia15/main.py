"""
=== Desafio do Dia 45 – Diagnóstico Inteligente do Sistema ===

Objetivo:
Criar um programa que analise o uso da CPU, memória e disco e gere um diagnóstico
automático sobre o estado do computador. O programa deve classificar o desempenho,
exibir recomendações e salvar um relatório com os resultados.

Funcionalidades:
1. Analisar CPU, memória e disco
2. Classificar o desempenho em "Bom", "Moderado" ou "Crítico"
3. Exibir recomendações automáticas
4. Salvar o diagnóstico em arquivo
5. Permitir novas análises ou encerramento
"""

import psutil
import os
import time







ARQUIVO = "diagnostico_sistema.txt"



def diagnosticar(valor, tipo):
    if valor < 50:
        return f"{tipo}: {valor}% - Bom"
    elif valor < 80:
        return f"{tipo}: {valor}% - Moderado"
    else:
        return f"{tipo}: {valor}% - Crítico"

def recomendacao(cpu, memoria, disco):
    dicas = []
    if cpu > 80:
        dicas.append("Feche programas pesados ou reinicie o computador.")
    if memoria > 80:
        dicas.append("Considere adicionar mais memoria RAM ou encerrar aplicativos não usados.")
    if disco > 85:
        dicas.append("Limpe arquivos temporários e desinstale programas desnecessários.")
    if not dicas:
        dicas.append("O sistema está funcionando normalmente.")
    return dicas

def salvar_relatorio(conteudo):
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(conteudo + "\n" + ("-" * 50) + "\n")





def executar_diagnostico():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=-= Diagnostico Inteligente do Sistema =-=\n")

    cpu = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory().percent
    disco = psutil.disk_usage('/').percent
    resultado = [
        diagnosticar(cpu, "Uso da CPU"),
        diagnosticar(memoria, "Uso da Memória"),
        diagnosticar(disco, "Uso do Disco")
    ]

    print("\n".join(resultado))
    print("\nRecomendações:")
    for dica in recomendacao(cpu, memoria, disco):
        print(f"- {dica}")

    relatorio = (
        f"\n=-= Diagnostico de {time.strftime('%d/%m/%Y %H:%M:%S')} =-=\n" +
        "\n".join(resultado) +
        "\n\nRecomendações:\n" + "\n".join(recomendacao(cpu, memoria, disco))
    )
    salvar_relatorio(relatorio)
    print("\nRelatorio salvo em 'diagnostico_sistema.txt'.")




def menu():
    while True:
        print("\n( 1 ) Executar diagnostico")
        print("( 2 ) Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            executar_diagnostico()
        elif opcao == "2":
            print("Encerrando diagnostico. Até a proxima verificação.")
            break
        else:
            print("Opção invalida, tente novamente.\n")








menu()
