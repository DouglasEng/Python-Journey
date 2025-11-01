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


def calcular_tendencia(valores):
    if len(valores) < 2:
        return 0
    diferencas = [valores[i] - valores[i - 1] for i in range(1, len(valores))]
    return round(sum(diferencas) / len(diferencas), 2)





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


print("\n=-= RELATORIO DE EVOLUÇÃO =-=\n")

pesos = [d["peso"] for d in dados_corporais.values()]
gorduras = [d["gordura"] for d in dados_corporais.values()]
tendencia_peso = calcular_tendencia(pesos)
tendencia_gordura = calcular_tendencia(gorduras)
print(f"Variação média de peso: {tendencia_peso:+.2f} kg/semana")
print(f"Variação média de gordura: {tendencia_gordura:+.2f}%/semana")

crescimento = {}
for grupo in dados_corporais[next(iter(dados_corporais))]["medidas"]:
    valores = [d["medidas"].get(grupo, 0) for d in dados_corporais.values()]
    tendencia = calcular_tendencia(valores)
    crescimento[grupo] = tendencia

print("\n=-= Crescimento Muscular por Grupo =-=")
for grupo, taxa in crescimento.items():
    print(f"{grupo}: {taxa:+.2f} cm/semana")
print("\n=-= Analise de Correlação (Treino x Crescimento) =-=")
for grupo, dados in treinos.items():
    taxa = crescimento.get(grupo, 0)
    if taxa > 0.3 and dados["eficiencia"] > 60:
        status = "Treino eficiente"
    elif taxa < 0 and dados["eficiencia"] < 40:
        status = "Treino ineficiente"
    else:
        status = "Neutro"
    print(f"{grupo}: {status} (Eficiencia {dados['eficiencia']} pts)")

ranking = sorted(treinos.items(), key=lambda x: x[1]['eficiencia'], reverse=True)
print("\n=-= Ranking de Eficiencia de Treino =-=")
for i, (grupo, dados) in enumerate(ranking, start=1):
    print(f"{i}. {grupo} – {dados['eficiencia']} pts")

print("\n=-= Projeção de Evolução =-=")
for grupo, taxa in crescimento.items():
    if taxa > 0:
        print(f"Se mantiver o ritmo, {grupo} crescerá +{taxa*4:.2f} cm no proximo mês.")
    else:
        print(f"{grupo} está em estagnação ou queda de rendimento.")

print("\nAnalise concluída. Continue evoluindo com inteligência!")