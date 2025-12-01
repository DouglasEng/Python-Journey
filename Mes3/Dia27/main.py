"""
=== Desafio do Dia 87 — Classificação de Produtividade com Pandas ===

Descrição:
Crie um DataFrame simulando hábitos de estudo e calcule a eficiência diária.
Depois, classifique cada dia em três níveis de produtividade: Alta, Média e Baixa.
Este desafio reforça o uso de funções apply, criação de categorias e filtragem.

Tarefas principais:
 - Criar DataFrame manualmente
 - Criar coluna de eficiência
 - Criar função de classificação
 - Identificar dias mais produtivos e dias críticos
 - Resumo final por categoria
"""




import pandas as pd




df = pd.DataFrame({
    "dia": ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"],
    "horas": [2.2, 1.0, 3.5, 2.0, 4.0, 0.8, 0.0],
    "foco": [7, 3, 9, 6, 8, 2, 1]
})
df["eficiencia"] = df["horas"] * (df["foco"] / 10)




def classificar_produtividade(valor):
    if valor >= 2.5:
        return "Alta"
    elif valor >= 1.0:
        return "Média"
    else:
        return "Baixa"

df["categoria_produtividade"] = df["eficiencia"].apply(classificar_produtividade)




print("\n=-= DataFrame atualizado =-=")
print(df)
print("\n=-= Dias com Alta produtividade =-=")
print(df[df["categoria_produtividade"] == "Alta"][["dia", "eficiencia"]])
print("\n=-= Dias criticos (baixa Pprodutividade) =-=")
print(df[df["categoria_produtividade"] == "Baixa"][["dia", "eficiencia"]])
print("\n -=- Resumo por categoria =-=")
print(df["categoria_produtividade"].value_counts())
