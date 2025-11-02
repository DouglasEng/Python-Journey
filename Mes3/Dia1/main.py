"""
=== Desafio do Dia 61 – Mini Analisador de Desempenho de Treino ===

Contexto:
Após estudarmos modelagem e simulação de dados (ex.: estratégias de treino no dia 60),
neste desafio vamos consolidar o aprendizado com um exercício focado em análise e visualização simples.

Objetivo:
Criar um pequeno script que analisa um conjunto de dados simulados sobre treinos,
extraindo métricas básicas e gerando insights estatísticos.

Conteúdos reforçados:
- Geração e estruturação de dados (listas e dicionários)
- Uso de compreensão de listas e funções built-in (sum, max, min, mean)
- Lógica condicional e classificação simples
- Introdução à análise de dados básica
"""






import random
from statistics import mean


def gerar_dados_treino(n=10):
    dados = []
    for i in range(1, n + 1):
        volume = random.randint(6, 30)
        intensidade = round(random.uniform(5.0, 10.0), 1)
        desempenho = round(volume * intensidade * random.uniform(0.7, 1.2), 2)
        dados.append({"sessao": i, "volume": volume, "intensidade": intensidade, "desempenho": desempenho})
    return dados


def analisar_dados(dados):
    volumes = [d["volume"] for d in dados]
    intensidades = [d["intensidade"] for d in dados]
    desempenhos = [d["desempenho"] for d in dados]
    resumo = {
        "volume_medio": round(mean(volumes), 2),
        "intensidade_media": round(mean(intensidades), 2),
        "desempenho_medio": round(mean(desempenhos), 2),
        "melhor_sessao": max(dados, key=lambda x: x["desempenho"]),
        "pior_sessao": min(dados, key=lambda x: x["desempenho"])
    }
    return resumo




def classificar_desempenho(valor, media):
    """Classifica o desempenho em relação a média."""
    if valor >= media * 1.1:
        return "Excelente"
    elif valor >= media * 0.9:
        return "Dentro da média"
    else:
        return "Abaixo da média"







def main():
    print("=-=- ANALISADOR DE DESEMPENHO =-=-")
    dados = gerar_dados_treino(10)
    resumo = analisar_dados(dados)

    print("\nResumo estatistico:")
    print(f"- Volume médio: {resumo['volume_medio']}")
    print(f"- Intensidade média: {resumo['intensidade_media']}")
    print(f"- Desempenho médio: {resumo['desempenho_medio']}")
    print("\nSessões:")
    for d in dados:
        status = classificar_desempenho(d["desempenho"], resumo["desempenho_medio"])
        print(f"Sessão {d['sessao']:>2} → Volume={d['volume']:>2} | Int={d['intensidade']:<4} | Desempenho={d['desempenho']:>6} → {status}")
    print("\nMelhor sessão:", resumo["melhor_sessao"])
    print("Pior sessão:", resumo["pior_sessao"])




if __name__ == "__main__":
    main()
