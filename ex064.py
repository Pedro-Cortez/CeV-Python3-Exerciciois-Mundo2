print('\033[33m--' * 9)
print('LEITOR DE NÚMEROS')
print('--' * 9, '\033[m')

num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número ou digite 999 para parar: '.format(cont)))
    cont += 1
    soma = soma + num
    if num == 999:
        soma = soma - 999
        cont_final = cont - 1
print('Você digitou {} números e soma entre eles é igual a {}.'.format(cont_final, soma))
