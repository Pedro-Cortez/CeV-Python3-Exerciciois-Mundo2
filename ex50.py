print('\033[1;31m-=-' * 10)
print('\tSoma de Números Pares')
print('-=-' * 10, '\033[m')

print('Digite 6 números inteiros:')
valor_a = int(input('1º número: '))
valor_b = int(input('2º número: '))
valor_c = int(input('3º número: '))
valor_d = int(input('4º número: '))
valor_e = int(input('5º número: '))
valor_f = int(input('6º número: '))
print('\033[1;31m-=-' * 10, '\033[m')

lista = [valor_a, valor_b, valor_c, valor_d, valor_e, valor_f]

soma = 0
c = 0
for cont in range(0, 6):
    if lista[cont] % 2 == 0:
        soma = soma + lista[cont]
        c += 1
print('A soma do(s) {} valor(es) par(es) é igual a {}.'.format(c, soma))

