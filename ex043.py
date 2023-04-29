import math
print('\033[1;35m--' * 9)
print('Calculadora de IMC')
print('--' * 9, '\033[m')
#Entrada do usuário
peso = float(input('Informe o peso (Kg): '))
altura = float(input('Informe o altura (m): '))
#Cálculo
imc = peso / (altura ** 2)
#Saída
print('Seu IMC é igual a {:.1f}. Você está '.format(imc), end='')
if imc < 18.5:
    print('\033[1;37mAbaixo do Peso Ideal\033[m')
elif imc >= 18.5 and imc < 25:
    print('no \033[1;32mPeso Ideal\033[m')
elif imc >= 25 and imc < 30:
    print('com \033[33mSobrepeso\033[m')
elif imc >= 30 and imc < 40:
    print('com \033[1;33mObesidade\033[m')
elif imc >= 40:
    print('com \033[1;31mObesidade Móbida\033[m')
