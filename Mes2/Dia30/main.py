"""
=== Desafio do Dia 60 – Sistema de Análise de Evolução no Fisiculturismo ===

Objetivo:
Construir um sistema completo que registre, analise e interprete dados de treinos e medidas corporais,
gerando relatórios de progresso, equilíbrio muscular e predições de evolução.

Contexto:
Atletas e praticantes de musculação muitas vezes não têm clareza sobre sua progressão real.
Este sistema visa fornecer uma visão analítica baseada em métricas objetivas de treino e corpo.

Funcionalidades:
1. Registro de dados corporais (peso, percentual de gordura, medidas por grupo muscular).
2. Registro detalhado de treinos (volume, intensidade, descanso, frequência semanal).
3. Cálculo de eficiência de treino e variação percentual por semana.
4. Análise de equilíbrio muscular e progresso corporal.
5. Predição simples de evolução com base em tendência linear (ganho/perda semanal média).
6. Geração de relatórios e ranking de grupos musculares com melhor evolução.

"""

def calcular_volume(series, repeticoes, carga):
    return series * repeticoes * carga

def calcular_eficiencia(volume, intensidade, descanso):
    eficiencia = (volume * intensidade) / (descanso + 1)
    return round(min(eficiencia / 100, 100), 2)








print("\n=-=- SISTEMA DE EVOLUÇÃO MUSCULAR =-=-\n")

dados_corporais = {}
while True:
    semana = input("Semana (ou ENTER para encerrar): ").strip()
    if not semana:
        break
    peso = float(input("Peso (kg): "))
    gordura = float(input("Percentual de gordura (%): "))
    medidas = {}
    while True:
        grupo = input("Grupo muscular (ex: Peito, Costas, Braço) ou ENTER para seguir: ").strip().capitalize()
        if not grupo:
            break
        medida = float(input(f"Medida atual de {grupo} (cm): "))
        medidas[grupo] = medida
    dados_corporais[semana] = {"peso": peso, "gordura": gordura, "medidas": medidas}
    print()

treinos = {}
print("\n=-= REGISTRO DE TREINOS =-=\n")
while True:
    grupo = input("Grupo muscular (ou ENTER para encerrar): ").strip().capitalize()
    if not grupo:
        break

    series = int(input("Séries: "))
    repeticoes = int(input("Repetições: "))
    carga = float(input("Carga (kg): "))
    intensidade = float(input("Intensidade (1-10): "))
    descanso = float(input("Descanso médio (seg): "))
    frequencia = int(input("Treinos por semana: "))
    volume = calcular_volume(series, repeticoes, carga)
    eficiencia = calcular_eficiencia(volume, intensidade, descanso)

    treinos[grupo] = {
        "volume": volume,
        "eficiencia": eficiencia,
        "frequencia": frequencia
    }
    print()
