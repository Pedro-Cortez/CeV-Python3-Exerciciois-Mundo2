num = 0
cont = 0
soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma = soma + num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e soma entre eles é igual a {}.'. format(cont, soma))
