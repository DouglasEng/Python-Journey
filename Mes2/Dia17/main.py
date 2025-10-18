"""
=== Desafio do Dia 47 – Simulador Ético de IA ===

Objetivo:
Criar um programa que simula como uma Inteligência Artificial toma decisões éticas
com base em diferentes valores (como honestidade, proteção, privacidade e eficiência).
O usuário escolhe uma situação moral e o sistema retorna a decisão da IA
segundo seus princípios predefinidos.

Funcionalidades:
1. O usuário escolhe uma situação ética.
2. A IA analisa o dilema com base em seus valores.
3. O programa exibe a decisão da IA com justificativa.
"""






def analisar_decisao(situacao, valores):    
    if situacao == "mentir_para_proteger":
        if valores["honestidade"] > valores["proteção"]:
            return "A IA escolheu dizer a verdade, priorizando a honestidade."
        else:
            return "A IA escolheu mentir para proteger alguém, priorizando a proteção."

    elif situacao == "usar_dados_sem_consentimento":
        if valores["privacidade"] > valores["eficiencia"]:
            return "A IA recusou o uso dos dados — prioriza a privacidade dos usuários."
        else:
            return "A IA usou os dados sem consentimento — prioriza a eficiência acima da privacidade."
        


    elif situacao == "salvar_um_ou_muitos":
        if valores["igualdade"] > valores["utilidade"]:
            return "A IA decidiu agir de forma igualitária, não priorizando quantidade."
        else:
            return "A IA optou por salvar o maior número possível — visão utilitarista."

    else:
        return "Situação não reconhecida pela IA."
    





def menu():
    print("\n=-=- Simulador Ético de IA -=-=")
    print("( 1 ) Mentir para proteger alguém")
    print("( 2 )  Usar dados sem consentimento")
    print("( 3 ) Escolher entre salvar uma pessoa ou muitas")
    opcao = input("Escolha uma situação (1-3): ")

    if opcao == "1":
        return "mentir_para_proteger"
    elif opcao == "2":
        return "usar_dados_sem_consentimento"
    elif opcao == "3":
        return "salvar_um_ou_muitos"
    else:
        return None

def main():
    valores_eticos = {
        "honestidade": 7,
        "proteção": 8,
        "privacidade": 9,
        "eficiencia": 5,
        "igualdade": 6,
        "utilidade": 7
    }




    situacao = menu()

    if situacao:
        resposta = analisar_decisao(situacao, valores_eticos)
        print(f"\nDecisão da IA: {resposta}")
    else:
        print("\nOpção invalida. Tente novamente.")






if __name__ == "__main__":
    main()
