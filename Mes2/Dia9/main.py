"""
=== Desafio do Dia 39 – Planejador de Refeições Semanais ===

Objetivo:
Criar um sistema que ajude o usuário a organizar suas refeições da semana,
registrar receitas favoritas e gerar um plano alimentar diário.

Funcionalidades:
1. Adicionar refeições por dia da semana
2. Listar refeições cadastradas
3. Visualizar plano semanal completo
4. Registrar receitas favoritas
5. Salvar tudo em arquivo para manter histórico
"""



import os


ARQUIVO_REFEICOES = "refeicoes_semana.txt"
ARQUIVO_RECEITAS = "receitas_favoritas.txt"

DIAS_SEMANA = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

def carregar_arquivo(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        return []
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f.readlines() if linha.strip()]

def salvar_arquivo(nome_arquivo, lista):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        for item in lista:
            f.write(item + "\n")




def adicionar_refeicao():
    dia = input(f"Escolha o dia da semana {DIAS_SEMANA}: ").strip().capitalize()
    if dia not in DIAS_SEMANA:
        print("Dia inválido!")
        return
    refeicao = input("Digite a refeição (ex: Almoço: Salada e Frango): ").strip()
    registro = f"{dia} | {refeicao}"
    refeicoes = carregar_arquivo(ARQUIVO_REFEICOES)
    refeicoes.append(registro)
    salvar_arquivo(ARQUIVO_REFEICOES, refeicoes)
    print(f"Refeição adicionada para {dia}.\n")







def listar_refeicoes():
    refeicoes = carregar_arquivo(ARQUIVO_REFEICOES)
    if not refeicoes:
        print("Nenhuma refeição registrada.\n")
        return
    print("\n=-= Refeições Registradas =-=\n")
    for r in refeicoes:
        print(r)
    print()



def visualizar_plano_semanal():
    refeicoes = carregar_arquivo(ARQUIVO_REFEICOES)
    if not refeicoes:
        print("Nenhuma refeição registrada para montar o plano.\n")
        return
    plano = {dia: [] for dia in DIAS_SEMANA}
    for linha in refeicoes:
        try:
            dia, refeicao = linha.split(" | ")
            plano[dia].append(refeicao)
        except ValueError:
            continue
    print("\n=-= Plano Semanal =-=\n")
    for dia in DIAS_SEMANA:
        print(f"{dia}:")
        if plano[dia]:
            for r in plano[dia]:
                print(f" - {r}")
        else:
            print(" - Nenhuma refeição registrada")
        print()




def adicionar_receita():
    receita = input("Digite o nome da receita favorita: ").strip()
    receitas = carregar_arquivo(ARQUIVO_RECEITAS)
    receitas.append(receita)
    salvar_arquivo(ARQUIVO_RECEITAS, receitas)
    print("Receita adicionada às favoritas!\n")




def ver_receitas():
    receitas = carregar_arquivo(ARQUIVO_RECEITAS)
    if not receitas:
        print("Nenhuma receita cadastrada.\n")
        return
    print("\n=-= Receitas Favoritas =-=\n")
    for r in receitas:
        print(f"- {r}")
    print()






def menu():
    while True:
        print("=-=- Planejador de Refeições Semanais =-=-")
        print("( 1 ) Adicionar refeição")
        print("( 2 ) Listar todas as refeições")
        print("( 3 ) Visualizar plano semanal")
        print("( 4 ) Adicionar receita favorita")
        print("( 5 ) Ver receitas favoritas")
        print("( 6 ) Sair")
        opcao = input("Escolha: ").strip()




        if opcao == "1":
            adicionar_refeicao()

        elif opcao == "2":
            listar_refeicoes()

        elif opcao == "3":
            visualizar_plano_semanal()

        elif opcao == "4":
            adicionar_receita()

        elif opcao == "5":
            ver_receitas()

        elif opcao == "6":
            print("Plano semanal salvo! Até a próxima!")
            break


        else:
            print("Opção inválida! Tente novamente.\n")








if __name__ == "__main__":
    menu()
