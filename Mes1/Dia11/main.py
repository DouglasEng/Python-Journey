"""
=== Desafio do Dia 11 – Sistema de Vendas com Estatísticas ===

Objetivo:
Criar um programa que simule o registro de vendas de uma loja e, ao final, exiba estatísticas detalhadas.

Regras:
1. O programa deve permitir cadastrar várias vendas no formato:
   - Nome do produto
   - Quantidade vendida
   - Preço unitário
2. Cada venda deve ser armazenada em uma estrutura de dados.
3. Ao encerrar o cadastro, o programa deve exibir:
   - Total de vendas realizadas
   - Faturamento total
   - Produto mais vendido (quantidade)
   - Produto mais lucrativo (valor total)
   - Ticket médio (faturamento / número de vendas)
   - Lista dos produtos ordenados por faturamento

"""





vendas = []

while True:
    print("\n-=-= Registro de Venda =-=-")
    produto = input("Nome do produto (ou 'sair' para encerrar): ").strip()
    if produto.lower() == "sair":
        break
    
    qtd = int(input("Quantidade vendida: "))
    preco = float(input("Preço unitário (R$): "))
    
    valor_total = qtd * preco
    
    vendas.append({
        "produto": produto,
        "quantidade": qtd,
        "preco": preco,
        "total": valor_total
    })

if vendas:
    faturamento_total = sum(v["total"] for v in vendas)
    total_vendas = len(vendas)
    ticket_medio = faturamento_total / total_vendas
    
    mais_vendido = max(vendas, key=lambda x: x["quantidade"])
    mais_lucrativo = max(vendas, key=lambda x: x["total"])
    ordenados = sorted(vendas, key=lambda x: x["total"], reverse=True)
    
    print("\n-=-= Estatísticas =-=-")
    print(f"Total de vendas registradas: {total_vendas}")
    print(f"Faturamento total: R$ {faturamento_total:.2f}")
    print(f"Ticket médio: R$ {ticket_medio:.2f}")
    print(f"Produto mais vendido: {mais_vendido['produto']} ({mais_vendido['quantidade']} unidades)")
    print(f"Produto mais lucrativo: {mais_lucrativo['produto']} (R$ {mais_lucrativo['total']:.2f})")
    
    print("\nProdutos ordenados por faturamento:")
    for v in ordenados:
        print(f"- {v['produto']}: R$ {v['total']:.2f}")
else:
    print("Nenhuma venda registrada.")
