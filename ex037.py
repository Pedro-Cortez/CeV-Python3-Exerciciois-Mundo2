print('\033[1;36m\t\tConversor de Bases')
print('-=-' * 13, '\033[m')
#Entrada do usuário
numero = int(input('Digite o valor que deseja converter: '))

#Escolha
print('\033[1;33m--' * 10)
print('\tMENU DE BASES')
print('--' * 10)
print('[1] Binário')
print('[2] Hexadecimal')
print('[3] Octal\033[m')
escolha = int(input('Informe a base de conversão do valor digitado: '))

#Resposta
if escolha == 1:
    binario = bin(numero)
    print('{}Você selecionou o sistema binário. Logo:'.format('\033[31m'))
    print('{} equivale a {}{}{}.'.format(numero, '\033[4;31m', binario[2:], '\033[m'))
elif escolha == 2:
    hexa = hex(numero)
    print('{}Você selecionou o sistema Hexadecimal. Logo:'.format('\033[31m'))
    print('{} equivale a {}{}{}.'.format(numero, '\033[4;31m', hexa[2:], '\033[m'))
elif escolha == 3:
    octal = oct(numero)
    print('{}Você selecionou o sistema Octal. Logo:'.format('\033[31m'))
    print('{} equivale a {}{}{}.'.format(numero, '\033[4;31m', octal[2:], '\033[m'))
else:
    print('{}Opção inválida! Tente Novamente.{}'.format('\033[1;31m', '\033[m'))
