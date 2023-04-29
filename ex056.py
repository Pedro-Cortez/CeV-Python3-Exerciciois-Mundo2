print('\033[1;33m-=-' * 12)
print('ANALISADOR DE PESSOAS: MODO COMPLETO')
print('-=-' * 12, '\033[m')

soma_idade = 0
idadeF = 0
idade_Hvelho = 0
nome_Hvelho = ''

print('Formulário de Cadastro')
for cont in range(1, 5):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    print('*' * 23)
    soma_idade += idade
    if cont == 1 and sexo in 'Mm':
        idade_Hvelho = idade
        nome_Hvelho = nome
    if sexo in 'Mm' and idade > idade_Hvelho:
        idade_Hvelho = idade
        nome_Hvelho = nome
    if sexo in 'Ff' and idade < 20:
        idadeF += 1

media_idade = soma_idade / 4

print('''Após análise é possível concluir que:
      1) A média de idade do grupo é {:.1f} anos.
      2) O homem mais velho chama-se {}.
      3) Há {} mulher(es) com menos de 20 anos'''.format(media_idade, nome_Hvelho, idadeF))

