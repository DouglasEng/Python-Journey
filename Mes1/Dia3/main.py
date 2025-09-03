'''

 Desafio: Validador de Senhas

O objetivo deste programa é verificar se uma senha criada pelo usuário atende aos critérios de segurança.


Regras obrigatórias para a senha ser considerada válida:

    1. Pelo menos 8 caracteres
    2. Contém ao menos 1 letra minúscula
    3. Contém ao menos 1 letra maiúscula
    4. Contém ao menos 1 número
    5. Contém ao menos 1 caractere especial (!@#$%^&*()-_+=)

O programa solicita a senha, testa todas as regras e informa o que está faltando até que a senha seja válida.

'''


import os

fatoracaoSenha = []

while True:
    senhaProposta = str(input('Digite sua senha').strip())
    lower = upper = 0
    for contador in range (0,len(senhaProposta)):
        fatoracaoSenha.append(senhaProposta[contador])
        if senhaProposta[contador].islower():
            lower = 1

        
    print(fatoracaoSenha)
    
    if len(fatoracaoSenha) < 8:
        print('Pelo menos 8 caracteres.')


    elif not any(char.islower() for char in senhaProposta):
        print("Pelo menos 1 letra minúscula.")

    elif not any(char.isupper() for char in senhaProposta):
        print("Pelo menos 1 letra maiúscula.")


    elif any(char in ['1', '2', '3','4','5','6','7','8','9'] for char in fatoracaoSenha) == False:
        print("Pelo menos 1 número")
    
    elif any(char in ['!','@','#','$','%','^','&','*','(',')','-','_','+','='] for char in fatoracaoSenha) == False:
        print("Pelo menos 1 caractere especial!")
    
    else:
        print('Senha válida!')
        break

    os.system('cls')

    fatoracaoSenha.clear()
