print('\033[36m==' * 10)
print('LEITOR DE NÚMEROS II')
print('==' * 10, '\033[m')

opcao = ''
soma = 0
cont = 0
maior = 0
menor = 0

while opcao != 'N':
    num = int(input('Digite um número inteiro: '))
    opcao = str(input('Gostaria de continuar? [S/N] ')).strip().upper()
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print('''Você digitou {} números:
Média = {:.1f}
Maior = {}
Menor = {}'''.format(cont, media, maior, menor))
