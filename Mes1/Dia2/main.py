'''
=== Gerenciador de Tarefas ===
1 - Adicionar tarefa
2 - Listar tarefas
3 - Atualizar tarefa
4 - Remover tarefa
5 - Sair

Escolha uma opção: 1
Digite o título da tarefa: Estudar Python
Tarefa adicionada com sucesso!

Escolha uma opção: 2
[1] Estudar Python - Pendente

Escolha uma opção: 3
Digite o ID da tarefa que deseja atualizar: 1
Novo título (ou enter para manter): Estudar Python avançado
Novo status (Pendente / Em andamento / Concluída): Em andamento

Escolha uma opção: 2
[1] Estudar Python avançado - Em andamento



'''

import os
from time import sleep

def adicionar():
    tarefa = str(input('Digite o titulo da tarefa: ').strip())
    tarefas.append([tarefa, status[0]])

def listar():
    for contador, items in enumerate(tarefas):
        print(f'{contador+1} {items[0]}  -  {items[1]}')
    


def atualizar():
    listar()
    opcaoRetirada = int(input('\nDigite a opção da tarefa: '))
    
    statusTarefaAtual = int(input('''
1 - Pendente
2 - Realizando
3 - Concluido
'''))

    if tarefas[opcaoRetirada-1][1] == status[statusTarefaAtual-1]:
        print('Não é possível alterar para um status semelhante.')
    
    elif statusTarefaAtual == 1:
        tarefas[opcaoRetirada-1][1] = status[0]
    elif statusTarefaAtual == 2:
        tarefas[opcaoRetirada-1][1] = status[1]
    elif statusTarefaAtual == 3:
        tarefas[opcaoRetirada-1][1] = status[2]
    else:
        print('Valor invalido!')
    cont = input('Aperte enter para continuar.')

def remover():
    listar()
    opcaoRetirada = int(input('\nDigite a opção da tarefa: '))

    
    tarefas.pop(opcaoRetirada-1)

status = ['Pendente', 'Realizando', 'Concluido']
tarefas = []
while True:
    os.system('cls')
    opcao = str(input('''=== Gerenciador de Tarefas ===
1 - Adicionar tarefa
2 - Listar tarefas
3 - Atualizar tarefa
4 - Remover tarefa
5 - Sair\n
    Digite o valor correspondente:  ''').strip())
    
    os.system('cls')
    if opcao == "1":
        adicionar()
    if opcao == "2":
        listar()
        cont = input('Aperte enter para continuar.')

    if opcao == "3":
        atualizar()

    if opcao == "4":
        remover()
    
    if opcao == "5":
        for contador in range(0,3):
            for contador2 in range(0,3):
                print("Carregando.", end='')
                print('.'*contador2)
                sleep(1)
                os.system('cls')
        print('Obrigado! Volte Sempre.')
        break
        


        
