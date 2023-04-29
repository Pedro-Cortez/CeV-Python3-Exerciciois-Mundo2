print('\033[1;33m=<>=' * 7)
print('DETECTOR DE NÚMEROS PRIMOS')
print('=<>=' * 7, '\033[m')

numero = int(input('Digite um número inteiro: '))

cont_div = 0

for cont in range(1, numero + 1):
    if numero % cont == 0:
        cont_div += 1
        print('\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(cont, '\033[m', end=' ')

print('\nO número {} foi divível {} vezes. '.format(numero, cont_div), end='')
if cont_div == 2:
    print('Logo, é PRIMO.')
elif cont_div > 2:
    print('Logo, NÃO É PRIMO.')


