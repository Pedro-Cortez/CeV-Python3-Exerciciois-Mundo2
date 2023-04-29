from time import sleep

print('\033[1;33m-=-' * 4)
print('CALCULADORA')
print('-=-' * 4, '\033[m')

opcao = 0

valorA = int(input('Informe o primeiro número: '))
valorB = int(input('Informe o segundo número: '))
while opcao != 5:
    print('''Escolha a operação que deseja realizar:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opcao = int(input('Informe a operação selecionada: '))
    if opcao == 1:
        soma = valorA + valorB
        print('Você escolheu somar. Então, {} + {} = {}'.format(valorA, valorB, soma))
        sleep(1)
    elif opcao == 2:
        mult = valorA * valorB
        print('Você escolheu multiplicação. Então, {} x {} = {}'.format(valorA, valorB, mult))
        sleep(1)
    elif opcao == 3:
        if valorA > valorB:
            print('Você escolheu maior. Então, o maior número é {}'.format(valorA))
            sleep(1)
        elif valorA < valorB:
            print('Você escolheu maior. Então, o maior número é {}'.format(valorB))
            sleep(1)
        else:
            print('Você escolheu maior. Mas, os números são iguais.')
            sleep(1)
    elif opcao == 4:
        print('-=-' * 14)
        print('Escolha novos números:')
        valorA = int(input('Informe o primeiro número: '))
        valorB = int(input('Informe o segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
        print('Fim do programa. Tchau!')
    else:
        print('Operação inválida! Selecione novamente.')
    print('-=-' * 14)



