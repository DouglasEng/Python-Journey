"""
=== Desafio do Dia 33 – Lembrete de Postura ===

Objetivo:
Criar um programa que ajude pessoas que passam muito tempo sentadas
(no computador, estudando ou trabalhando) a corrigirem a postura em intervalos regulares.

Funcionalidades:
1. O usuário define o intervalo de lembrete (em minutos).
2. A cada intervalo, o programa emite um alerta sonoro e textual.
3. Sugere diferentes dicas de postura a cada aviso.
4. Pode ser encerrado manualmente (Ctrl+C).
5. Útil para quem deseja evitar dores nas costas e melhorar a saúde ao estudar ou trabalhar.
"""




import time
import random

import pyttsx3



engine = pyttsx3.init()

DICAS = [
    "Endireite as costas e mantenha os ombros relaxados.",
    "Ajuste a altura da tela para a linha dos olhos.",
    "Mantenha os pés apoiados no chão.",
    "Faça uma pausa rápida e alongue o pescoço.",
    "Evite cruzar as pernas para melhorar a circulação.",
    "Relaxe os ombros e solte a tensão."
]

def falar(mensagem):
    engine.say(mensagem)
    engine.runAndWait()



def lembrete_postura(intervalo):
    print(f"\nLembrete de postura iniciado! Aviso a cada {intervalo} minutos.\n")
    try:
        while True:
            time.sleep(intervalo * 60)
            dica = random.choice(DICAS)
            print(f"\nLembre-se de ajustar sua postura!\nDica: {dica}\n")
            falar("Lembre-se de ajustar sua postura. " + dica)
    except KeyboardInterrupt:
        print("\nPrograma encerrado. Cuide bem da sua saúde postural!")



def menu():
    print("=-=- Lembrete de Postura =-=-")
    intervalo = int(input("Defina o intervalo de lembrete (em minutos): ").strip())
    lembrete_postura(intervalo)





if __name__ == "__main__":
    menu()
