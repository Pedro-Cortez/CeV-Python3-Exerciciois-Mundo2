print('\033[1;32m=' * 20)
print('Comparando Números')
print('=' * 20, '\033[m')
#Entrada do usuário
numeroA = int(input('Digite o primeiro valor: '))
numeroB = int(input('Digite o segundo valor: '))
#Respostas
if numeroA > numeroB:
    print('O PRIMEIRO é maior valor.')
elif numeroB > numeroA:
    print('O SEGUNDO é o maior valor.')
else:
    print('Não existe valor maior, os dois são IGUAIS')
