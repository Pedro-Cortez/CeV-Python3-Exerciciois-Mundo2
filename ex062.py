print('\033[1;35m-=-' * 5)
print('GERADOR DE P.A.')
print('-=-' * 5, '\033[m')
termo1 = int(input('Primeiro termo da P.A.: '))
razao = int(input('Razão: '))

termo_qtd = 0
cont = 1
termo_n = 10

while termo_n != 0:
    termo_qtd = termo_qtd + termo_n
    while cont <= termo_qtd:
        print(termo1, end=' → ')
        cont += 1
        termo1 = termo1 + razao
    print('PAUSA')
    termo_n = int(input('Gostaria de incluir quantos termos? '))
print('\033[35mP.A. finalizada no {} termos mostrados.\033[m'.format(termo_qtd))

