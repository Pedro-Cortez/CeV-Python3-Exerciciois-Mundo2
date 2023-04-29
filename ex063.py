print('\033[31m=' * 22)
print('SEQUÊNCIA DE FIBONACCI')
print('=' * 22, '\033[m')

termos = int(input('Informe quantos termos gostaria de exibir: '))

fib1 = 0
fib2 = 1
cont = 3

print('{} → {}'. format(fib1, fib2), end=' → ')
while cont <= termos:
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
    cont += 1
    print(fib3, end=' → ')
print('FIM')
