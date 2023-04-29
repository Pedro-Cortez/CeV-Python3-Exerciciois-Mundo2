print('\033[1;37m---' * 9)
print('Cálculo de Média Bimestral')
print('---' * 9, '\033[m')
#Entrada do usuário
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
#Cálculo da média
media = (nota1 + nota2) / 2
#Saídas
print('---' * 9)
print('Média bimestral: {:.2f}'.format(media))
if media < 5.0:
    print('Aluno {}REPROVADO{}!'.format('\033[1;31m', '\033[m'))
elif media >= 5.0 and media < 7.0:
    print('Aluno em {}RECUPERAÇÃO{}!'.format('\033[1;33m', '\033[m'))
elif media >= 7.0:
    print('Aluno {}APROVADO{}!'.format('\033[1;34m', '\033[m'))
