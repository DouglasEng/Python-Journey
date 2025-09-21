"""
=== Desafio do Dia 20 – Bloco de Notas Rápido ===

Objetivo:
Criar um programa simples para registrar anotações rápidas.

Regras:
1. O usuário pode escrever uma anotação curta.
2. A anotação é salva em "notas.txt".
3. O usuário pode listar todas as anotações já registradas.
4. O programa continua em loop até o usuário sair.
"""




import os

ARQUIVO = "notas.txt"

def salvar_nota(nota):
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(nota + "\n")



def listar_notas():
    if not os.path.exists(ARQUIVO):
        print("\nNenhuma nota registrada ainda.\n")
        return
    
    print("\n=-=- Suas Notas -=-=")
    

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        for i, linha in enumerate(f, start=1):
            print(f"{i}. {linha.strip()}")

def menu():
    while True:
        print("\nBloco de Notas")
        print("1. Adicionar nota")
        print("2. Listar notas")
        print("3. Sair")
        opcao = input("Escolha: ").strip()
        

        if opcao == "1":
            nota = input("Digite sua anotação: ").strip()
            if nota:
                salvar_nota(nota)
                print("Nota salva!")


        elif opcao == "2":
            listar_notas()


        elif opcao == "3":
            print("Saindo do bloco de notas...")
            break


        else:
            print("Opção inválida! Tente de novo.")




menu()
