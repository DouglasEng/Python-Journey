"""
=== Desafio do Dia 57 – Laboratório de DNA Sintético ===

Objetivo:
Criar um sistema simples que gera, armazena e analisa sequências de DNA sintético,
permitindo observar mutações e distribuições de bases genéticas.

Contexto:
Na biotecnologia e na ciência de dados, simular cadeias genéticas e analisar mutações
é uma das formas de testar modelos preditivos e estudar comportamento de dados biológicos.
Aqui, você controlará um "mini laboratório" genético digital.

Funcionalidades:
1. Gerar uma sequência de DNA aleatória com tamanho definido.
2. Exibir a porcentagem de cada base (A, T, C, G).
3. Aplicar mutações aleatórias em uma sequência existente.
4. Salvar e carregar sequências em um arquivo "dna_lab.txt".
5. Sair do programa.
"""





import os
import random



ARQUIVO = "dna_lab.txt"
BASES = ["A", "T", "C", "G"]




def gerar_dna(tamanho):
    return "".join(random.choice(BASES) for _ in range(tamanho))


def contar_bases(seq):
    total = len(seq)
    contagem = {b: seq.count(b) for b in BASES}
    porcentagem = {b: round((contagem[b] / total) * 100, 2) for b in BASES}
    return porcentagem



def mutar(seq, taxa=0.05):
    seq = list(seq)
    for i in range(len(seq)):
        if random.random() < taxa:
            seq[i] = random.choice(BASES)
    return "".join(seq)



def salvar(seq):
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(seq + "\n")



def carregar():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f]
    



def menu():
    while True:
        print("\n=-=- Laboratorio de DNA Sintetico =-=-")
        print("( 1 ) Gerar nova sequencia")
        print("( 2 ) Analisar uma sequencia")
        print("( 3 ) Aplicar mutação")
        print("( 4 ) Ver historico salvo")
        print("( 5 ) Sair")
        op = input("Escolha: ").strip()


        if op == "1":
            tamanho = int(input("Tamanho da sequencia: "))
            dna = gerar_dna(tamanho)
            salvar(dna)
            print(f"\nNova sequencia gerada: {dna}")





        elif op == "2":
            historico = carregar()
            if not historico:
                print("Nenhuma sequencia salva ainda.")
                continue
            for i, seq in enumerate(historico, 1):
                print(f"{i}. {seq}")
            esc = int(input("Escolha o número da sequencia: ")) - 1
            if 0 <= esc < len(historico):
                analise = contar_bases(historico[esc])
                print("Distribuição de bases:", analise)
            else:
                print("Escolha invalida.")




        elif op == "3":
            historico = carregar()
            if not historico:
                print("Nenhuma sequencia disponível.")
                continue
            for i, seq in enumerate(historico, 1):
                print(f"{i}. {seq}")
            esc = int(input("Escolha o numero da sequencia: ")) - 1
            if 0 <= esc < len(historico):
                nova = mutar(historico[esc])
                salvar(nova)
                print(f"Sequencia mutada: {nova}")
            else:
                print("Escolha invalida.")



        elif op == "4":
            historico = carregar()
            if historico:
                print("\n=-= Sequencias Salvas =-=")
                for seq in historico:
                    print(seq)
            else:
                print("Nenhum DNA registrado ainda.")

        elif op == "5":
            print("Encerrando o laboratorio genetico...")
            break


        else:
            print("Opção invalida! Tente novamente.")




menu()
