print('\t\033[1;35mNova Tabuada')
print('<>' * 10, '\033[m')

tab = int(input('Qual tabuada você quer ver? '))

for cont in range(1, 11):
    print('{} x {:2} = {}'.format(tab, cont, tab * cont))
print('\033[1;35m<>' * 10, '\033[m')
