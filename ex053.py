print('\033[1;35m-=-' * 9)
print('IDENTIFICADOR DE PALÍDROMO')
print('-=-' * 9, '\033[m')

frase = str(input('Digite uma frase para análise: \n')).strip().upper()

frase_div = frase.split()
junto = ''.join(frase_div)

print('O inverso da frase {} é {}.'.format(junto[0::], junto[::-1]), end=' ')

if junto[0::] == junto[::-1]:
    print('Logo, é um PALÍNDROMO.')
else:
    print('Logo, NÃO É UM PALÍNDROMO.')
