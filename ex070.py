print('\033[1;32m-=-' * 10)
print('\t\tLojão do Povo')
print('-=-' * 10, '\033[m')

total = preco_mil = cont = menor_preco = 0
barato = ' '
while True:
    merc = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Devo continuar a venda? [S/N] ')).strip().upper()[0]
    total += preco
    cont += 1
    if cont == 1:
        menor_preco = preco
        barato = merc
    else:
        if preco < menor_preco:
            menor_preco = preco
            barato = merc
    if preco > 1000.0:
        preco_mil += 1
    if opcao == 'N':
        break
print('-=-' * 5, 'RESUMO DA VENDA', '-=-' * 5)
print(f'Valor total da venda: R$ {total:.2f}')
print(f'Produtos com valor superior a mil reais: {preco_mil}')
print(f'Produto mais barato: {barato} - R$ {menor_preco:.2f}')
