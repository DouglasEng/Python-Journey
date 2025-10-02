"""
=== Desafio do Dia 31 – Lembrete de Medicamentos com Voz ===

Objetivo:
Criar um programa simples que ajude pessoas com deficiência visual ou dificuldade de
lembrar horários a tomar seus medicamentos, usando lembretes sonoros e mensagens de texto.

Funcionalidades:
1. Cadastrar horários e nomes de medicamentos.
2. Alertar no horário certo com mensagem no terminal e voz sintetizada.
3. Permitir checar os próximos horários programados.
4. Salvar histórico de alertas para acompanhar doses tomadas.
"""

import time
import json
import pyttsx3
from datetime import datetime

ARQUIVO = "medicamentos.json"

engine = pyttsx3.init()





def falar(mensagem):
    """Lê a mensagem em voz alta"""
    engine.say(mensagem)
    engine.runAndWait()



def carregar_medicamentos():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []



def salvar_medicamentos(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=2, ensure_ascii=False)



def cadastrar_medicamento():
    nome = input("Nome do medicamento: ").strip()
    horario = input("Horário de tomar (HH:MM, 24h): ").strip()
    med = {"nome": nome, "horario": horario}
    meds = carregar_medicamentos()
    meds.append(med)
    salvar_medicamentos(meds)
    print(f"{nome} cadastrado para {horario}.")



def mostrar_proximos():
    meds = carregar_medicamentos()
    if not meds:
        print("Nenhum medicamento cadastrado.")
        return
    print("\nPróximos horários de medicação:")
    agora = datetime.now()
    for med in meds:
        h, m = map(int, med["horario"].split(":"))
        med_time = agora.replace(hour=h, minute=m, second=0, microsecond=0)
        if med_time < agora:
            med_time += timedelta(days=1)
        delta = med_time - agora
        print(f"{med['nome']} em {med['horario']} (em {delta.seconds//3600}h {(delta.seconds//60)%60}min)")



def monitorar():
    """Loop contínuo para alertar o usuário no horário certo"""
    print("Monitoramento iniciado. Pressione Ctrl+C para sair.")
    meds = carregar_medicamentos()
    try:
        while True:
            agora = datetime.now()
            hora_min = agora.strftime("%H:%M")
            for med in meds:
                if med["horario"] == hora_min:
                    msg = f"Hora de tomar {med['nome']}!"
                    print(msg)
                    falar(msg)
                    # prevenir alerta multiplo no mesmo minuto
                    time.sleep(60)
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nMonitoramento encerrado.")




def menu():
    while True:
        print("\n=-=- Lembrete de Medicamentos =-=-")
        print("(1) Cadastrar medicamento")
        print("(2) Ver próximos horários")
        print("(3) Iniciar monitoramento")
        print("(4) Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            cadastrar_medicamento()

        elif opcao == "2":
            mostrar_proximos()

        elif opcao == "3":
            monitorar()

        elif opcao == "4":
            print("Encerrando.")
            break

        else:
            print("Opção inválida!")



if __name__ == "__main__":
    menu()
