"""
=== Desafio do Dia 32 – Lembrete de Hidratação ===

Objetivo:
Criar um programa simples que ajude pessoas a lembrarem de beber água regularmente,
emitindo alertas em intervalos configurados pelo usuário.

Funcionalidades:
1. O usuário define o intervalo de tempo entre os lembretes (em minutos).
2. O programa emite um alerta sonoro e textual a cada intervalo.
3. Permite encerrar o programa manualmente (Ctrl+C).
4. Útil para estudantes, trabalhadores ou pessoas que esquecem de se hidratar.

"""

import time
import pyttsx3

engine = pyttsx3.init()

def falar(mensagem):
    """Faz o computador falar a mensagem em voz alta"""
    engine.say(mensagem)
    engine.runAndWait()




def lembrete_agua(intervalo):
    print(f"\nLembrete de hidratação iniciado! Um aviso será dado a cada {intervalo} minutos.\n")
    try:
        while True:
            time.sleep(intervalo * 60)
            msg = "Hora de beber água!"
            print(f"\n{msg}\n")
            falar(msg)
    except KeyboardInterrupt:
        print("\nPrograma encerrado. Continue se hidratando!")




def menu():
    print("=-=- Lembrete de Hidratação =-=-")
    intervalo = int(input("Defina o intervalo de lembrete (em minutos): ").strip())
    lembrete_agua(intervalo)







if __name__ == "__main__":
    menu()
