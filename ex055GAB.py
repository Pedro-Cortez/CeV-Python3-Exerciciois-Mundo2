print('\033[1;35m==' * 8)
print('COMPARANDO PESOS')
print('==' * 8, '\033[m')

pesado = 0
leve = 0

for cont in range(1, 6):
    peso = float(input('Quantos quilos pesa a {}ª pessoa? '.format(cont)))
    if cont == 1:
        pesado = peso
        leve = peso
    else:
        if peso > pesado:
            pesado = peso
        if peso < leve:
            leve = peso
print('\033[35mA pessoa mais pesada tem {:.1f} kg e a mais leve tem {:.1f} kg.\033[m'.format(pesado, leve))