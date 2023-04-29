print('\033[1;33m-=-' *12)
print('ANÁLISE DE DADOS - GRUPO DE PESSOAS')
print('-=-' * 12, '\033[m')

mais18 = 0
homem = 0
mulher20 = 0
while True:
    print('-' * 25)
    print('\tCADASTRO PESSOAL')
    print('-' * 25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Gostaria de continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homem += 1
    if idade < 20 and sexo == 'F':
        mulher20 += 1
    if opcao == 'N':
        break
print('-' * 25)
print(f'Pessoas com mais de 18 anos: {mais18}')
print(f'Quantidade total de homens: {homem}')
print(f'Mulheres com menos de 20 anos: {mulher20}')
