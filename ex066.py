print('\033[36m==' * 10)
print('LEITOR DE NÚMEROS II')
print('==' * 10, '\033[m')

cont = 0
soma = 0
while True:
    num = int(input('Digite um número inteiro [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} números, com soma igual a {soma}.')
