"""
=== Desafio do Dia 81 — Visualizações com Matplotlib (sem CSV) ===

Descrição:
Este desafio expande a análise feita com Pandas adicionando visualizações
gráficas usando Matplotlib, ainda sem uso de arquivos externos.
A proposta é simular dados de vendas semanais e gerar gráficos simples
(mas úteis) para compreender tendências, distribuição e comparações.

Tarefas:
 - Criar DataFrame com dados semanais de vendas
 - Plotar:
     • Gráfico de linha da evolução diária de vendas
     • Gráfico de barras comparando faturamento por produto
     • Gráfico de pizza com participação percentual das vendas
 - Manter foco na aplicação prática de Pandas + Matplotlib
"""





import pandas as pd
import matplotlib.pyplot as plt





def criar_base():
    data = {
        "day": ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"],
        "product": ["Copo", "Copo", "Tampa", "Prato", "Copo", "Tampa", "Prato"],
        "units_sold": [120, 150, 90, 200, 170, 110, 140],
        "unit_price": [1.50, 1.50, 2.00, 3.50, 1.50, 2.00, 3.50]
    }
    df = pd.DataFrame(data)
    df["total_revenue"] = df["units_sold"] * df["unit_price"]
    return df







def gerar_graficos(df):
    plt.figure(figsize=(8, 4))
    plt.plot(df["day"], df["units_sold"], marker="o")
    plt.title("Evolução diária das vendas")
    plt.xlabel("Dia da semana")
    plt.ylabel("Unidades vendidas")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    faturamento_produto = df.groupby("product")["total_revenue"].sum()

    plt.figure(figsize=(7, 4))
    plt.bar(faturamento_produto.index, faturamento_produto.values)
    plt.title("Faturamento por produto")
    plt.xlabel("Produto")
    plt.ylabel("Faturamento total (R$)")
    plt.tight_layout()
    plt.show()

    vendas_produto = df.groupby("product")["units_sold"].sum()

    plt.figure(figsize=(6, 6))
    plt.pie(
        vendas_produto.values,
        labels=vendas_produto.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Participação de vendas por produto")
    plt.tight_layout()
    plt.show()





def main():
    df = criar_base()
    print("\n=-=- BASE DE VENDAS -=-")
    print(df)
    gerar_graficos(df)








if __name__ == "__main__":
    main()
