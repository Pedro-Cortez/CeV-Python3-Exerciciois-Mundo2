print('\033[33m=' * 18)
print('TABUADA INTERATIVA')
print('=' * 18, '\033[m')

while True:
    tab = int(input('Qual tabuada gostaria de ver? '))
    print('-' * 35)
    if tab < 0:
        break
    for cont in range(1, 11):
        print(f'{tab} x {cont:2} = {tab * cont}')
    print('-' * 35)
print('\033[33mFim do programa. Continue estudando!\033[m')
