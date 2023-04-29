print('\033[1;32m-=-' * 9)
print('CADASTRO MASCULINO/FEMININO')
print('-=-' * 9, '\033[m')

sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Opção Inválida! Informe o sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} gravado com sucesso!'.format(sexo))
