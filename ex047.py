print('\033[1;34m-=-' * 11)
print('\tContador de Números Pares')
print('-=-' * 11, '\033[m')

for cont in range(1, 51):
    if cont % 2 == 0:
        print(cont, end=' ')
print('{}- FIM.{}'.format('\033[1;34m', '\033[m'))

# Gabarito
for cont in range(2, 51, 2):
    print(cont, end=' ')
print('FIM')
