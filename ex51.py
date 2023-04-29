print('\033[1;34m-=-' * 7)
print('10 TERMOS DE UMA P.A.')
print('-=-' * 7, '\033[m')

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

an = a1 + (10 - 1) * r

for cont in range(a1, an + r, r):
    print(cont, end=' → ')
print('FIM')
