"""
=== Desafio do Dia 9 – Mini Analisador de Vendas ===

Objetivo:
Criar um programa que permita cadastrar vendas, listar todas, calcular estatísticas simples
e exportar os dados para um arquivo CSV.

Funcionalidades:
1. Adicionar nova venda (produto, quantidade, valor unitário)
2. Listar todas as vendas cadastradas
3. Calcular faturamento total
4. Mostrar o produto mais vendido
5. Exportar os dados para um arquivo CSV
6. Sair

"""

import csv
import os

vendas = []

def adicionar_venda():
    produto = input("Produto: ").strip()
    quantidade = int(input("Quantidade: "))
    valor = float(input("Valor unitário (R$): "))

    vendas.append({
        "produto": produto,
        "quantidade": quantidade,
        "valor": valor
    })

    print("Venda adicionada com sucesso!")




def listar_vendas():

    if not vendas:
        print("Nenhuma venda cadastrada.")
        return
    
    print('=-'*4, 'Lista de Vendas', '=-'*4)
    
    for i, v in enumerate(vendas, 1):
        print(f"[{i}] {v['produto']} - {v['quantidade']} un. x R${v['valor']:.2f}")



def faturamento_total():
    total = sum(v["quantidade"] * v["valor"] for v in vendas)

    print(f"\nFaturamento total: R${total:.2f}")




def produto_mais_vendido():
    if not vendas:
        print("Nenhuma venda cadastrada.")
        return
    
    ranking = {}
    for v in vendas:
        ranking[v["produto"]] = ranking.get(v["produto"], 0) + v["quantidade"]
    mais_vendido = max(ranking, key=ranking.get)

    print(f"\nProduto mais vendido: {mais_vendido} ({ranking[mais_vendido]} unidades)")



def exportar_csv():
    if not vendas:
        print("Nenhuma venda cadastrada para exportar.")
        return
    
    with open("vendas.csv", "w", newline="", encoding="utf-8") as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=["produto", "quantidade", "valor"])
        writer.writeheader()
        writer.writerows(vendas)

    print("Dados exportados para 'vendas.csv'.")





while True:
    print('=-'*4, "Analisador de Vendas", '=-'*4)
    print('''
1 - Adicionar venda
2 - Listar vendas
3 - Faturamento total
4 - Produto mais vendido
5 - Exportar para CSV
6 - Sair
          ''')
          

    opcao = input("Escolha uma opção: ").strip()
    os.system("cls" if os.name == "nt" else "clear")

    if opcao == "1":
        adicionar_venda()
    elif opcao == "2":
        listar_vendas()
    elif opcao == "3":
        faturamento_total()
    elif opcao == "4":
        produto_mais_vendido()
    elif opcao == "5":
        exportar_csv()
    elif opcao == "6":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
