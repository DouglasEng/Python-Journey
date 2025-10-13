"""
=== Desafio do Dia 42 – Analisador de DNA ===

Objetivo:
Criar um programa que leia uma sequência de DNA, valide se ela é biologicamente correta
(composta apenas por A, T, C e G), e realize uma série de análises automáticas sobre ela.

Funcionalidades:
1. Validar se a sequência contém apenas nucleotídeos válidos (A, T, C, G)
2. Calcular a porcentagem de cada base nitrogenada
3. Encontrar o complemento reverso da sequência (regra biológica: A↔T, C↔G)
4. Traduzir a sequência para RNA (T → U)
5. Salvar a análise completa em um arquivo de texto ("analises_dna.txt")
"""

import os






ARQUIVO = "analises_dna.txt"






def validar_dna(seq):
    """verifica se a sequencia contem apenas nucleotideos validos."""
    for base in seq:
        if base not in "ATCG":
            return False
    return True




def porcentagem_bases(seq):
    """calcula a porcentagem de cada base no DNA"""
    total = len(seq)
    return {base: (seq.count(base) / total) * 100 for base in "ATCG"}




def complemento_reverso(seq):
    """retorna o complemento reverso do DNA (A↔T, C↔G)."""
    mapa = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(mapa[b] for b in reversed(seq))




def transcrever_para_rna(seq):
    """converte DNA em RNA (T → U)"""
    return seq.replace("T", "U")




def salvar_analise(seq, porcentagens, comp_rev, rna):
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"=-= Analise de Sequencia de DNA =-=\n")
        f.write(f"Sequencia original: {seq}\n")
        f.write(f"Comprimento: {len(seq)} bases\n")
        f.write("\n--- Porcentagem de bases ---\n")
        for base, perc in porcentagens.items():
            f.write(f"{base}: {perc:.2f}%\n")
        f.write(f"\nComplemento reverso: {comp_rev}\n")
        f.write(f"Sequencia de RNA: {rna}\n")
        f.write(f"{'-'*40}\n\n")







def main():
    print("=-=- Analisador de DNA =-=-")
    seq = input("Digite a sequencia de DNA (apenas A, T, C, G): ").upper().strip()

    if not validar_dna(seq):
        print("\nSequência invalida! Use apenas A, T, C e G.")
        return

    porcentagens = porcentagem_bases(seq)
    comp_rev = complemento_reverso(seq)
    rna = transcrever_para_rna(seq)
    print("\n=-= Resultados da Analise =-=")
    for base, perc in porcentagens.items():
        print(f"{base}: {perc:.2f}%")
    print(f"\nComplemento reverso: {comp_rev}")
    print(f"Sequencia de RNA: {rna}")
    salvar_analise(seq, porcentagens, comp_rev, rna)
    print("\nAnalise salva em 'analises_dna.txt'.")








if __name__ == "__main__":
    main()
