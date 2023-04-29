print('\t\t\033[1;33mCalculadora de Descontos\033[m')
print('---' * 15)
#Entrada do usuário
preco = float(input('Digite o valor da compra: R$ '))
print('---' * 15)
print('''Opções de pagamento:
    [1] À vista dinheiro/cheque
    [2] À vista cartão
    [3] Parcelado no cartão''')
opcao = int(input('Selecione a forma de pagamento: '))
if opcao == 1:
    promo = preco - (preco * 10 / 100)
    print('Seu produto custa R${:.2f}, com desconto de 10% custará R${:.2f}.'.format(preco, promo))
elif opcao == 2:
    promo = preco - (preco * 5 / 100)
    print('Seu produto custa R${:.2f}, com desconto de 5% custará R${:.2f}.'.format(preco, promo))
elif opcao == 3:
    parcela = int(input('Quantidade de parcelas: '))
    if parcela == 2:
        mes = preco / 2
        print('Seu produto custa R${:.2f} e será parcelado em {}x de R${:.2f} sem juros.'.format(preco, parcela, mes))
    elif parcela >= 3:
        promo = preco + (preco * 20 / 100)
        mes = promo / parcela
        print('Seu produto custa R${:.2f} e será parcelado em {}x de R${:.2f} com juros.'.format(preco, parcela, mes))
        print('Com acréscimo de 20% de juros, o valor final do produto será R${:.2f}.'.format(promo))
else:
    print('\33[1;31mForma de pagamento inválida! Tente novamente.\033[m')
    