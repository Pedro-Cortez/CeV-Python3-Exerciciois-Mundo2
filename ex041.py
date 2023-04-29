from datetime import date
print('\033[1;36m---' * 13)
print('Confederação Nacional de Natação')
print('Categoria de Atletas conforme a Idade')
print('---' * 13, '\033[m')
#Entrada do usuário
atual = date.today().year
nasc = int(input('Informe o ano de nascimento do atleta: '))
#Saída
print('---' * 13)
idade = atual - nasc
print('Idade do atleta: {} anos'.format(idade))
if idade <= 9:
    print('Categoria: Mirim')
elif idade > 9 and idade <= 14:
    print('Categoria: Infantil')
elif idade > 14 and idade <= 19:
    print('Categoria: Júnior')
elif idade > 19 and idade <= 25:
    print('Categoria: Sênior')
elif idade > 25:
    print('Categoria: Master')
