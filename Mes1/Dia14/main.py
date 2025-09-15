"""
=== Desafio do Dia 14 – Analisador de Notas ===

Objetivo:
Ler um arquivo de notas e gerar estatísticas simples.

Regras:
1. O arquivo "notas.txt" contém apenas números (um por linha).
2. O programa deve:
   - Calcular a média das notas
   - Encontrar a maior e menor nota
   - Contar quantas notas estão acima da média
3. O resultado deve ser salvo em "resultado.txt"
4. Usar tratamento de erros caso o arquivo não exista.

"""

import os
caminho_notas = os.path.join(os.path.dirname(__file__), "notas.txt")

try:
    with open(caminho_notas, "r", encoding="utf-8") as f:
        notas = [float(linha.strip()) for linha in f if linha.strip()]
    if not notas:
        raise ValueError("O arquivo está vazio!")


    media = sum(notas) / len(notas)
    maior = max(notas)
    menor = min(notas)
    acima_media = sum(1 for n in notas if n > media)
    resultado = (
        f"Média: {media:.2f}\n"
        f"Maior nota: {maior}\n"
        f"Menor nota: {menor}\n"
        f"Notas acima da média: {acima_media}"
    )
    caminho_resultado = os.path.join(os.path.dirname(__file__), "resultado.txt")
    with open(caminho_resultado, "w", encoding="utf-8") as f:
        f.write(resultado)


    print("Análise concluída! Confira o arquivo resultado.txt.")




except FileNotFoundError:
    print("Arquivo 'notas.txt' não encontrado!")
except ValueError as e:
    print(f"Erro: {e}")
