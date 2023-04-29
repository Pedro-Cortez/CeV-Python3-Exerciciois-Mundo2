import random
from emoji import emojize
from time import sleep
print('{:-^20}'.format(' JoKenPO '))
# Entrada das jogadas
print('Opções de movimento:')
print('[0] Pedra', emojize(':mount_fuji:'))
print('[1] Papel', emojize(':page_facing_up:'))
print('[2] Tesoura', emojize(':scissors:'))
jogada = ('Pedra', 'Papel', 'Tesoura')
comp = random.randint(0, 2)
player = int(input('Faça sua jogada: '))
print('{:^20}'.format('JO'))
sleep(1)
print('{:^20}'.format('KEN'))
sleep(1)
print('{:^20}'.format('PÔ!'))
# Saída
print('<<<' * 9)
print('Computador escolheu {}.'.format(jogada[comp]))
print('Jogador escolheu {}.'.format(jogada[player]))
print('>>>' * 9)
if comp == 0:
    if player == 0:
        print('{}Temos um empate!{}'.format('\033[1;33m', '\033[m'))
    elif player == 1:
        print('{}Jogador Venceu!{}'.format('\033[1;32m', '\033[m'))
    elif player == 2:
        print('{}Computador Venceu!{}'.format('\033[1;35m', '\033[m'))
    else:
        print('{}Jogada Inválida!{}'.format('\033[1;31m', '\033[m'))
elif comp == 1:
    if player == 0:
        print('{}Computador Venceu!{}'.format('\033[1;35m', '\033[m'))
    elif player == 1:
        print('{}Temos um empate!{}'.format('\033[1;33m', '\033[m'))
    elif player == 2:
        print('{}Jogador Venceu!{}'.format('\033[1;32m', '\033[m'))
    else:
        print('{}Jogada Inválida!{}'.format('\033[1;31m', '\033[m'))
elif comp == 2:
    if player == 0:
        print('{}Jogador Venceu!{}'.format('\033[1;32m', '\033[m'))
    elif player == 1:
        print('{}Computador Venceu!{}'.format('\033[1;35m', '\033[m'))
    elif player == 2:
        print('{}Temos um empate!{}'.format('\033[1;33m', '\033[m'))
    else:
        print('{}Jogada Inválida!{}'.format('\033[1;31m', '\033[m'))
