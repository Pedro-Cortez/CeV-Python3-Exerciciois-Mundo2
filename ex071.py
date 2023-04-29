print('\033[1;33m=' * 59)
print('BANCO CALOTE'.center(60, ' '))
print('=' * 11, 'Disponível R$ 50, R$ 20, R$ 10, R$1', '=' * 11, '\033[m')
saque = int(input('Digite a quantia para saque: R$ '))
ced50 = saque / 50
if int(ced50) != 0:
    print(f'Cédulas R$50: {int(ced50)}')
resto50 = saque % 50
ced20 = resto50 / 20
if int(ced20) != 0:
    print(f'Cédula R$20: {int(ced20)}')
resto20 = resto50 % 20
ced10 = resto20 / 10
if int(ced10) != 0:
    print(f'Cédula R$10: {int(ced10)}')
resto10 = resto20 % 10
ced1 = resto10
if int(ced1) != 0:
    print(f'Cédula R$1: {int(ced1)}')
print('\033[1;33m', end='')
print(' Banco Calote agradece a preferência '.center(66, '='))
