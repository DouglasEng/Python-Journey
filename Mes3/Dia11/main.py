"""
=== DESAFIO DO DIA 71 — Mini Análise de Atendimento (Pandas) ===

Neste desafio, continuamos nossa jornada prática com Pandas.
A ideia é manter exercícios introdutórios, porém aplicáveis a
um cenário real — algo simples, mas com utilidade prática.

Objetivo:
- Criar um pequeno DataFrame representando atendimentos de clientes.
- Realizar operações básicas, porém essenciais na análise de dados:
    • filtrar linhas
    • calcular médias
    • agrupar informações
    • gerar pequenas estatísticas úteis

Esse tipo de prática reflete análises reais usadas em negócios pequenos.
"""




import pandas as pd





dados = {
    "cliente": ["Ana", "Bruno", "Ana", "Carlos", "Bruno", "Daniela"],
    "tempo_atendimento_min": [12, 20, 15, 30, 18, 10],
    "satisfacao": [4, 5, 4, 3, 5, 4],
    "tipo_servico": ["Corte", "Barba", "Corte", "Tintura", "Corte", "Sobrancelha"]
}




df = pd.DataFrame(dados)

print("\nDATAFRAME INICIAL:")
print(df)
media_tempo = df["tempo_atendimento_min"].mean()
print("\n⏱️ Tempo médio de atendimento:", media_tempo)


satisfacao_alta = df[df["satisfacao"] >= 4]
print("\Atendimentos com alta satisfação:")
print(satisfacao_alta)


media_por_servico = df.groupby("tipo_servico")["tempo_atendimento_min"].mean()
print("\nMédia de tempo por tipo de serviço:")
print(media_por_servico)

contagem_clientes = df["cliente"].value_counts()
print("\nQuantidade de atendimentos por cliente:")
print(contagem_clientes)
