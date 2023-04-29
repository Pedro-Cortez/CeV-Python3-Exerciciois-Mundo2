print('\033[1;33m-=-' * 12)
print('Avaliador de empréstimo imobiliário')
print('-=-' * 12)
#Entradas do usuário
imovel = float(input('{}Valor do imóvel: R$'.format('\033[m')))
anos = int(input('Duração do contrato (anos): '))
renda = float(input('Renda mensal do contratante: R$'))

#Cálculos
meses = anos * 12
parcela = imovel / meses
renda_limite = renda * (30 / 100)

#Respostas
if parcela <= renda_limite:
    print('{}Financiamento aprovado!'.format('\033[34m'))
    print('Sua renda de R${:.2f} é suficente para aprovar parcelas de R${:.2f} mensais!{}'.format(renda, parcela,'\033[m'))
else:
    print('{}Seu financimento foi negado!'.format('\033[31m'))
    print('A renda mensal de R${:.2f} é não sufuciente para aprovar parcelas de R${:.2f} mensais{}'.format(renda, parcela, '\033[m'))
