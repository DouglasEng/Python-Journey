"""
=== Desafio do Dia 56 – Limpeza de Dados de Vendas  ===

Objetivo:
Criar um programa em Python que leia um arquivo CSV simples de vendas,
trate dados incorretos (valores vazios, preços negativos, etc.)
e gere um novo arquivo "limpo", pronto para análise.

Contexto:
Antes de analisar dados, é essencial realizar uma etapa de “limpeza” (data cleaning).
Esse processo garante que os números usados sejam confiáveis e úteis para gerar insights.
Esse é o primeiro passo em direção à Análise e Ciência de Dados.

Funcionalidades:
1. Ler um arquivo CSV de vendas (ex: vendas.csv)
2. Corrigir valores ausentes e preços negativos
3. Remover linhas incompletas ou inválidas
4. Salvar os dados tratados em um novo arquivo CSV ("vendas_limpo.csv")
5. Exibir um pequeno resumo do processo
"""






import csv


def limpar_dados_vendas(arquivo_entrada, arquivo_saida):
    dados_limpos = []
    total_linhas = 0
    linhas_invalidas = 0

    with open(arquivo_entrada, 'r', encoding='utf-8') as entrada:
        leitor = csv.DictReader(entrada)
        for linha in leitor:
            total_linhas += 1

            produto = linha.get('produto', '').strip()
            quantidade = linha.get('quantidade', '').strip()
            preco = linha.get('preco', '').strip()

            #verifica se tem campos vazios
            if not produto or not quantidade or not preco:
                linhas_invalidas += 1
                continue

            try:
                quantidade = int(quantidade)
                preco = float(preco)
            except ValueError:
                linhas_invalidas += 1
                continue

            if quantidade < 0 or preco < 0:
                linhas_invalidas += 1
                continue

            dados_limpos.append({
                'produto': produto,
                'quantidade': quantidade,
                'preco': preco
            })

    with open(arquivo_saida, 'w', newline='', encoding='utf-8') as saida:
        campos = ['produto', 'quantidade', 'preco']
        escritor = csv.DictWriter(saida, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(dados_limpos)




    print(f"\n=-= LIMPEZA CONCLUiDA =-=")
    print(f"Total de registros: {total_linhas}")
    print(f"Registros validos: {len(dados_limpos)}")
    print(f"Registros removidos: {linhas_invalidas}")
    print(f"Arquivo limpo salvo como: {arquivo_saida}")






if __name__ == "__main__":
    print("=-=- LIMPEZA DE DADOS DE VENDAS =-=-\n")
    arquivo_entrada = input("Digite o nome do arquivo CSV de entrada: ").strip()
    limpar_dados_vendas(arquivo_entrada, "vendas_limpo.csv")
