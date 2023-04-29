from time import sleep

print('\033[1;34m=' * 20)
print('DESCOBRINDO FATORIAL')
print('=' * 20, '\033[m')

fatorial = int(input('Informe número para cálculo do fatorial: '))

fator1 = fatorial - 1
produto = fatorial * fator1

while fator1 != 1:
    fator1 = fator1 - 1
    produto = produto * fator1
print('\033[34mCalculando...')
sleep(1)
print('{}! é igual a  {}.\033[m'.format(fatorial, produto))

