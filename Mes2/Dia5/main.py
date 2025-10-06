"""
=== Desafio do Dia 35 – Gerador de Sonhos Surreais ===

Objetivo:
Criar um programa que gera sonhos aleatórios com base em palavras e temas.
O usuário pode escolher um tipo de sonho e o programa criará uma narrativa surreal.

Funcionalidades:
1. O usuário escolhe o tipo de sonho (ex: tranquilo, estranho, assustador, futurista).
2. O programa mistura frases e palavras de forma aleatória para criar um sonho único.
3. O sonho é exibido de forma "narrativa", com pequenos intervalos entre as frases.
4. O sonho gerado é salvo automaticamente em um arquivo "meus_sonhos.txt".
5. O usuário pode visualizar todos os sonhos já registrados.
"""





import random
import time
import os


ARQUIVO = "meus_sonhos.txt"
fragmentos = {
    "tranquilo": [
        "você caminhava por um campo de flores que cantavam em harmonia",
        "um vento suave contava segredos antigos",
        "as nuvens se moviam devagar, desenhando rostos sorridentes",
        "o mar refletia as cores de um pôr do sol que nunca terminava"
    ],
    "estranho": [
        "uma girafa tocava violino em cima de um telhado",
        "o chão era feito de teclas de piano, e cada passo emitia um som diferente",
        "você falava com o reflexo de si mesmo, mas ele não te respondia",
        "as estrelas desciam do céu para conversar sobre filosofia"
    ],
    "assustador": [
        "as luzes piscavam e um sussurro dizia seu nome repetidamente",
        "você corria, mas o chão se movia junto com você",
        "um espelho mostrava alguém que não era você",
        "vozes distantes pediam para você não acordar"
    ],
    "futurista": [
        "as cidades flutuavam sobre oceanos metálicos",
        "robôs serviam café enquanto discutiam arte abstrata",
        "as pessoas se comunicavam apenas com pensamentos coloridos",
        "o céu era coberto por anúncios em hologramas"
    ]
}




def gerar_sonho(tipo):
    if tipo not in fragmentos:
        print("Tipo inválido.\n")
        return None

    sonho = []
    for _ in range(random.randint(3, 5)):
        sonho.append(random.choice(fragmentos[tipo]))

    print("\nGerando sonho...\n")
    time.sleep(1.5)


    for frase in sonho:
        print(frase.capitalize() + ".")
        time.sleep(1.5)



    sonho_texto = " ".join(frase.capitalize() + "." for frase in sonho)
    salvar_sonho(tipo, sonho_texto)
    print("\nSonho registrado!\n")
    return sonho_texto




def salvar_sonho(tipo, texto):
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"[{tipo.upper()}] {texto}\n\n")




def ver_sonhos():
    if not os.path.exists(ARQUIVO):
        print("\nNenhum sonho registrado ainda.\n")
        return
    

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        print("\n=-= Sonhos Registrados =-=\n")
        print(f.read())



def menu():
    while True:
        print("=-=- Gerador de Sonhos Surreais =-==")
        print("( 1 ) Criar um novo sonho")
        print("( 2 ) Ver sonhos registrados")
        print("( 3 ) Sair")
        escolha = input("Escolha: ").strip()



        if escolha == "1":
            print("\nTipos disponíveis: tranquilo, estranho, assustador, futurista")
            tipo = input("Escolha o tipo de sonho: ").strip().lower()
            gerar_sonho(tipo)

        elif escolha == "2":
            ver_sonhos()

        elif escolha == "3":
            print("Até o próximo sonho...")
            break


        else:
            print("Opção inválida.\n")





if __name__ == "__main__":
    menu()
