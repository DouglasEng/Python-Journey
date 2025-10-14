"""
=== Desafio do Dia 43 – Simulador de Crescimento Populacional ===

Objetivo:
Criar um programa que simule o crescimento populacional de uma espécie ao longo de um
determinado número de anos, levando em conta taxa de natalidade, mortalidade e capacidade
máxima do ambiente (limite ecológico).

Conceito biológico:
Na ecologia, o crescimento populacional tende a seguir um padrão logístico, limitado pela
capacidade de suporte do ambiente (K). Este programa simplifica esse modelo para
mostrar como o equilíbrio populacional é atingido ao longo do tempo.

Fórmula utilizada:
Nova população = População atual + (taxa_natalidade * atual) - (taxa_mortalidade * atual)
Se o valor ultrapassar a capacidade máxima, a população é ajustada para o limite.

Funcionalidades:
1. Solicitar dados iniciais do usuário:
   - População inicial
   - Taxa de natalidade (%)
   - Taxa de mortalidade (%)
   - Capacidade máxima do ambiente
   - Quantidade de anos para simulação
2. Exibir a população estimada ano a ano
3. Salvar os resultados no arquivo 'crescimento_populacional.txt'
"""


import os




ARQUIVO = "crescimento_populacional.txt"

def simular_crescimento(pop_inicial, taxa_natalidade, taxa_mortalidade, capacidade, anos):
    populacao = pop_inicial
    resultados = []
    for ano in range(1, anos + 1):
        nascimentos = populacao * (taxa_natalidade / 100)
        mortes = populacao * (taxa_mortalidade / 100)
        populacao += nascimentos - mortes
        if populacao > capacidade:
            populacao = capacidade  # limite ecologico
        resultados.append((ano, round(populacao)))
    return resultados



def salvar_resultados(resultados, pop_inicial, taxa_natalidade, taxa_mortalidade, capacidade):
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write("=-= Simulação de Crescimento Populacional =-=\n")
        f.write(f"População inicial: {pop_inicial}\n")
        f.write(f"Taxa de natalidade: {taxa_natalidade}%\n")
        f.write(f"Taxa de mortalidade: {taxa_mortalidade}%\n")
        f.write(f"Capacidade máxima: {capacidade}\n\n")
        for ano, pop in resultados:
            f.write(f"Ano {ano}: {pop} indivíduos\n")
        f.write(f"{'-'*40}\n\n")







def main():
    print("=-=- Simulador de Crescimento Populacional =-=-")
    try:
        pop_inicial = int(input("População inicial: "))
        taxa_natalidade = float(input("Taxa de natalidade (%): "))
        taxa_mortalidade = float(input("Taxa de mortalidade (%): "))
        capacidade = int(input("Capacidade máxima do ambiente: "))
        anos = int(input("Anos de simulação: "))
    except ValueError:
        print("Entrada inválida! Use apenas números.")
        return
    resultados = simular_crescimento(pop_inicial, taxa_natalidade, taxa_mortalidade, capacidade, anos)






    print("\n=-= Resultados =-=")
    for ano, pop in resultados:
        print(f"Ano {ano}: {pop} indivíduos")

    salvar_resultados(resultados, pop_inicial, taxa_natalidade, taxa_mortalidade, capacidade)
    print(f"\nRelatório salvo em '{ARQUIVO}'.")






if __name__ == "__main__":
    main()
