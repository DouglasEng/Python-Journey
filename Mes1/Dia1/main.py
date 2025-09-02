"""
Desafio: Analisador de Notas de Alunos

Descrição:
Este código tem como objetivo calcular a média das notas de uma lista de alunos, 
informar se cada aluno está aprovado ou reprovado, e gerar um ranking com os alunos 
ordenados da maior para a menor média.

Objetivo do exercício:
- Praticar estruturas de dados (dicionários e listas).
- Manipular loops e condicionais.
- Calcular médias e trabalhar com ordenação de listas.
- Produzir saída formatada e legível para o usuário.

"""

alunos = {
    "Alice": [7, 8, 9],
    "Bruno": [6, 5, 7],
    "Carla": [10, 9, 10],
    "Pedro": [2,4,5],
    'Douglas': [4, 6,2]
}

alunoLista = []

print('=-'*20)

for nome, contador in alunos.items():
    media = sum(contador)/len(contador)
    if media >=7:
        print(f'{nome.capitalize()}: média {media:.2f} - Aprovado')
    else:
        print(f'{nome.capitalize()}: média {media:.2f} - Reprovado')

    alunoLista.append([nome,media])

print('=-'*20)

alunoLista.sort(key=lambda item: item[1], reverse=True)
print(f'\nLista dos alunos com notas ordenadas: \n')

for contador in alunoLista:
    print(f'{contador[0]}: {contador[1]:.2f}')

print('=-'*20)
