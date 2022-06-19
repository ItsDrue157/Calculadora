# blibliotecas
import time
import getpass
from unittest import case


def protecao_de_senha():
    master_password = str('carlos')
    senha = str(input('Qual a sua senha? '))
    if senha != master_password:
        exit()
    else:
        print('Senha negada')




def calculadora():
    operation = input('''
Selecione abaixo as operacoes:
+ Para adicao
- para subtracao
* para multiplicacao
/ para divisao
''')

    # Declarando variaveis
    numero_1 = input('Entre o primeiro numero: ')
    numero_2 = input('Entre o segundo numero : ')

    if numero_1 is not [0,1,2,3,4,5,6,7,8,9]: 
        print("Teste")    




    # Operacoes abaixo
    if operation == '+':
        print('{} + {} = '.format(numero_1, numero_2))
        print(numero_1 + numero_2)

    elif operation == '-':
        print('{} - {} = '.format(numero_1, numero_2))
        print(numero_1 - numero_2)

    elif operation == '*':
        print('{} * {} = '.format(numero_1, numero_2))
        print(numero_1 * numero_2)

    elif operation == '/':

        print('{} / {} = '.format(numero_1, numero_2))
        print(numero_1 / numero_2)

    # Se a entrada de dados for diferente de +, - , * ,/ .
    else:
        operation != '+, -, *, /'
        print("Opcao negada tente novamente"), exit()
    # Pergunta se deseja fazer novamente
    de_novo()

# Fazendo a pergunta para se deseja refazer o calculo


def de_novo():
    calc_de_novo = input('''
Deseja calcular novamente?
Selecione Y para sim ou N para nao.
''')

    # Aceitar 'y' ou 'Y' para adicionar na .upper()
    if calc_de_novo.upper() == 'Y':
        calculadora()

    # Aceitar 'n' ou 'N' para adicionar na .upper()
    elif calc_de_novo.upper() == 'N':
        print('Ate mais.')

    else:
        calc_de_novo()


# chamando as funcoes
#protecao_de_senha()
calculadora()
de_novo()


# tempo para permanecer a resposta na tela
time.sleep(5)
