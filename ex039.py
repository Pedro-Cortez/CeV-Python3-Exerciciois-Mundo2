from datetime import date
print('\033[1;32m=' * 30)
print('Idade para Alistamento Militar')
print('=' * 30, '\033[m')

sexo = str(input('Digite o sexo do usuário: ')).lower()
if sexo == 'feminino':
    print('{}Você está dispensada do alistamento militar obrigatório!{}'.format('\033[1;33m', '\033[m'))
elif sexo == 'masculino':
    nasc = int(input('Informe o ano de nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - nasc
    if idade < 18:
        saldo = 18 - idade
        alista = ano_atual + saldo
        print('Você tem {} anos. Ainda faltam {}{} ano(s){} para o seu alistamento.'.format(idade, '\033[4;31m', saldo, '\033[m'))
        print('Você deverá se alistar em {}.'.format(alista))
    elif idade == 18:
        print('Você tem {}18 anos{}. Realize o seu alistamento imediatamente!'.format('\033[34m', '\033[m'))
    else:
        saldo = idade - 18
        alista = ano_atual - saldo
        print('Você tem {} anos. Seu alistamento deveria ter sido realizado há {}{} ano(s){}.'.format(idade, '\033[4;31m', saldo, '\033[m'))
        print('Você deveria ter se alistado em {}.'.format(alista))

