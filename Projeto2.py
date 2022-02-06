'''
Pequeno projeto usando o if/elif statement em python, cujo 
gera um valor aleatório de 1 a 10.
Que só para de rodar quando o usúario acerta o número gerado.
'''

import random

valor_aleatorio = random.randint(1, 10)
acerto = False
while acerto == False:
    chute = int(input('Chute um valor de 1 a 10: '))
    if chute > valor_aleatorio:
        print('O chute foi maior que o valor!')
    elif chute < valor_aleatorio:
            print('O chute foi menor que o valor!')
    elif chute == valor_aleatorio:
        acerto = True
        print('Acertou miseravii!!!!')