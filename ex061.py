print('\033[1;35m-=-' * 8)
print('10 TERMOS DE UMA P.A. II')
print('-=-' * 8, '\033[m')
termo1 = int(input('Primeiro termo da P.A.: '))
razao = int(input('Razão: '))

cont = 1

while cont <= 10:
    print(termo1, end=' → ')
    cont += 1
    termo1 = termo1 + razao
print('FIM')
