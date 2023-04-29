print('\033[1;35mJOGO DE ADIVINHAÇÃO')
print('-=-' * 7, '\033[m')

import random
from time import sleep

#Sorteio
comp = random.randint(0, 10)

#Escolha do usuário
print('Adivinhe, em qual número estou pensado?\n')
palpite = int(input('Escolha um número de 0 a 10: '))
print('\nPROCESSANDO...\n')
sleep(1)
cont = 0
while palpite != comp:
    print('\033[31mQue pena! Você errou!', end=' ')
    if palpite < comp:
        print('\033[31mTente um número maior.')
    elif palpite > comp:
        print('\033[31mTente um número menor.')
    palpite = int(input('\033[mEscolha um número de 0 a 10: '))
    cont += 1
print('\n\033[32mVocê acertou com {} tentativa(s). Parabéns!\033[m'.format(cont + 1))
