"""
=== Desafio do Dia 44 – Monitor de Recursos do Sistema ===

Objetivo:
Criar um programa em Python que monitore o uso da CPU, memória e disco,
exibindo as informações em tempo real. O programa deve atualizar os dados
periodicamente e permitir que o usuário encerre a execução manualmente.

Funcionalidades:
1. Exibir uso da CPU (%)
2. Exibir uso de memória (total, usada e livre)
3. Exibir uso de disco (%)
4. Atualizar as informações a cada 2 segundos
5. Encerrar com Ctrl+C
"""





import psutil
import time
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def monitorar_sistema():
    while True:
        limpar_tela()
        print("=-=- Monitor de Recursos do Sistema -=-=\n")
        #cpu    
        uso_cpu = psutil.cpu_percent(interval=1)
        print(f"Uso da CPU: {uso_cpu}%")
        # memoria
        memoria = psutil.virtual_memory()
        total = memoria.total / (1024 ** 2)
        usada = memoria.used / (1024 ** 2)
        livre = memoria.available / (1024 ** 2)
        print(f"Memória Total: {total:.2f} MB")
        print(f"Memória Usada: {usada:.2f} MB")
        print(f"Memória Livre: {livre:.2f} MB")
        # disco
        disco = psutil.disk_usage('/')
        print(f"Uso do Disco: {disco.percent}%")
        print("\nPressione Ctrl+C para encerrar...")
        time.sleep(2)





try:
    monitorar_sistema()
except KeyboardInterrupt:
    print("\nMonitor encerrado pelo usuário.")
