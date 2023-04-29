print('\033[1;33m-=-' * 11)
print('\tSomador de Múltiplos de 3')
print('-=-' * 11, '\033[m')

print('Intervalo 1 - 500:')
soma = 0
for cont in range(3, 501, 3):
    if cont % 2 != 0:
        soma = soma + cont
print(soma)
