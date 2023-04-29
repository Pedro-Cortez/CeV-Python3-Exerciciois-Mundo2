import time
import emoji

print('\t\033[1;35mCONTAGEM REGRESSIVA')
print('-=-' * 9, '\033[m')
for cont in range(10, -1, -1):
    print(cont)
    time.sleep(1)
print(emoji.emojize(':fireworks:') * 10)
print('\tFELIZ ANO NOVO!')
print(emoji.emojize(':sparkler:') * 10)

