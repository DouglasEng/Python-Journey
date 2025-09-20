"""
=== Desafio do Dia 19 – Gerador de Profecias Aleatórias ===

Objetivo:
Criar um programa que gera profecias místicas e engraçadas de forma aleatória.

Regras:
1. Cada profecia é formada por 3 partes escolhidas aleatoriamente:
   - Início misterioso
   - Meio dramático
   - Final inesperado
2. O usuário pode pedir novas profecias ou sair.
3. Todas as profecias são salvas no arquivo "profecias.txt".
"""

import os
import random




ARQUIVO = "profecias.txt"

inicios = [
    "Quando a lua brilhar em vermelho,",
    "Se o vento soprar do norte,",
    "No dia em que as sombras dançarem,",
    "Quando os gatos cantarem à meia-noite,",
    "Se você ouvir passos atrás de si,"
]

meios = [
    "um segredo antigo será revelado",
    "um desafio inesperado surgirá",
    "alguém próximo mostrará sua verdadeira face",
    "um portal oculto poderá se abrir",
    "a sorte mudará de lado"
]

fins = [
    "e você terá que escolher sabiamente.",
    "mas ninguém acreditará em você.",
    "e tudo parecerá um sonho.",
    "levando ao início de uma nova era.",
    "e será tarde demais para voltar atrás."
]



def gerar_profecia():
    return f"{random.choice(inicios)} {random.choice(meios)} {random.choice(fins)}"


def salvar_profecia(profecia):
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(profecia + "\n")



def ver_historico():
    if not os.path.exists(ARQUIVO):
        print("\nNenhuma profecia registrada ainda.\n")
        return
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        print("\n=-=- Histórico de Profecias =-=-\n")
        print(f.read())


def menu():
    while True:
        print("=-=- Gerador de Profecias Místicas -=-=")
        print("1. Receber uma profecia")
        print("2. Ver histórico de profecias")
        print("3. Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            profecia = gerar_profecia()
            print(f"\n{profecia}\n")
            salvar_profecia(profecia)
        elif opcao == "2":
            ver_historico()
        elif opcao == "3":
            print("Até a próxima revelação cósmica!")
            break
        else:
            print("Opção inválida!\n")






menu()
