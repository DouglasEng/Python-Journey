"""
=== Desafio do Dia 67 — Visualizador de Médias com Gráfico de Barras ===

Descrição:
Desenvolva um programa que receba notas ou valores de diferentes grupos
(por exemplo, turmas, treinos, produtos, etc.), calcule a média de cada grupo
e exiba um gráfico de barras comparando os resultados.

Objetivos:
 - Trabalhar com listas e dicionários
 - Usar o módulo matplotlib para visualização
 - Praticar cálculos estatísticos simples
"""




import matplotlib.pyplot as plt
import statistics




def coletar_dados():
    dados = {}
    while True:
        nome = input("\nNome do grupo (ou 'sair' para encerrar): ").strip()
        if nome.lower() == 'sair':
            break
        valores = [float(x) for x in input(f"Digite os valores de {nome} separados por espaço: ").split()]
        dados[nome] = valores
    return dados



def calcular_medias(dados):
    medias = {grupo: statistics.mean(valores) for grupo, valores in dados.items()}
    return medias




def exibir_grafico(medias):
    grupos = list(medias.keys())
    valores = list(medias.values())
    plt.bar(grupos, valores, color='skyblue')
    plt.title("Comparativo de Médias por Grupo")
    plt.xlabel("Grupos")
    plt.ylabel("Média")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


print("=-=- Comparador visual de médias =-=-")
dados = coletar_dados()
if dados:
    medias = calcular_medias(dados)
    print("\nMédias calculadas:")
    for grupo, media in medias.items():
        print(f"{grupo}: {media:.2f}")
    exibir_grafico(medias)
else:
    print("Nenhum grupo informado. Encerrando programa.")
