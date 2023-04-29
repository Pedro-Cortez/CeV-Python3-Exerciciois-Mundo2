from random import randint
from emoji import emojize

print('\033[31m-=-' * 10)
print('\t\tPAR OU ÍMPAR')
print('-=-' * 10, '\033[m')

cont = 0
while True:
    play = int(input('Digite um valor [0 a 10]: '))
    comp = randint(0, 10)
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Par ou Ìmpar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {play} e computador {comp}. O total é igual a {play + comp}.')
    print('-=-' * 20)
    if opcao == 'P':
        if (play + comp) % 2 == 0:
            print('Parabéns! Você venceu.\nQuero uma revanche, jogue novamente...')
            cont += 1
        else:
            print(emojize('Gamer Over! Até a próxima.:hand_with_fingers_splayed:'))
            break
    elif opcao == 'I':
        if (play + comp) % 2 == 1:
            print('Parabéns! Você venceu.\nQuero revanche, jogue novamente...')
            cont += 1
        else:
            print(emojize('Game Over! Até a próxima.:hand_with_fingers_splayed:'))
            break
    print('-=-' * 20)
print(f'Você ganhou {cont} rodadas.')
