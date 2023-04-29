import datetime

print('\033[1;34m=' * 21)
print('ANALISANDO MAIORIDADE')
print('=' * 21, '\033[m')

hoje = datetime.date.today().year
menor = 0
maior = 0

print('Digite o ano de nascimento de cada pessoa do grupo')
for cont in range(1, 8):
    ano = int(input('{}º pessoa: '.format(cont)))
    if hoje - ano < 21:
        menor += 1
    else:
        maior += 1
print('No grupo de 7 pessoas há {} pessoa(s) MENOR(ES) idade e {} MAIOR(ES) de idade.'.format(menor, maior))
