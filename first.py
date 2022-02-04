# Feito de maneira iniciante.
# Jogo de adivinhação de números - Escolha um número da tabela dada e responda as perguntas feitas pelo Robô Python
# Divirta-se
from time import sleep
import emoji
print('\033[31m-=-\033[m'*15,'\033[34mVamos jogar!\033[m','\033[31m-=-\033[m'*15)
sleep(1.5)
print(emoji.emojize(':robot:: \033[31mPense em um número entre 1 e 63 e eu vou adivinhar!\033[m'))
sleep(1)
print('...')
sleep(2)
print('..')
sleep(1)
print('.')
sleep(0.5)
print(emoji.emojize(':robot:: \033[31mPensou?\033[m'))
sleep(3)
print(emoji.emojize(':robot:: \033[31mAgora responda com SIM ou NÃO se o número que você pensou está, ou não, na tabela\033[m\n'))
sleep(3)
num = 0
table1 = [[1, 3, 5, 7, 9, 11, 13, 15], [17, 19, 21, 23, 25, 27, 29, 31], [33, 35, 37, 39, 41, 43, 45, 47], [49, 51, 53, 55, 57, 59, 61, 63]]
table2 = [[2, 3, 6, 7, 10, 11, 14, 15], [18, 19, 22, 23, 26, 27, 30, 31], [34, 35, 38, 39, 42, 43, 46, 47], [50, 51, 54, 55, 58, 59, 62, 63]]
table3 = [[4, 5, 6, 7, 12, 13, 14, 15], [20, 21, 22,23, 28, 29, 30, 31], [36, 37, 38, 39, 44, 45, 46, 47], [52, 53, 54, 55, 60, 61, 62, 63]]
table4 = [[8, 9, 10, 11, 12, 13, 14,15], [24, 25, 26, 27, 28, 29, 30, 31], [40, 41, 42, 43, 44, 45, 46, 47], [56, 57, 58, 59, 60, 61, 62, 63]]
table5 = [[16, 17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30, 31], [48, 49, 50, 51, 52, 53, 54, 55], [56, 57, 58, 59, 60, 61, 62, 63]]
table6 = [[32, 33, 34, 35, 36, 37, 38, 39], [40, 41, 42, 43, 44, 45, 46, 47], [48, 49, 50, 51, 52, 53, 54, 55], [56, 57, 58, 59, 60, 61, 62, 63]]
for table in range(0, 6):
    print('\n\033[7m','-' * 20, f'TABELA {table+1}', '-' * 20,'\033[m')
    if table == 0:
        for numintable, value in enumerate(table1):
            print(table1[numintable])
    if table == 1:
        for numintable, value in enumerate(table2):
            print(table2[numintable])
    if table == 2:
        for numintable, value in enumerate(table3):
            print(table3[numintable])
    if table == 3:
        for numintable, value in enumerate(table4):
            print(table4[numintable])
    if table == 4:
        for numintable, value in enumerate(table5):
            print(table5[numintable])
    if table == 5:
        for numintable, value in enumerate(table6):
            print(table6[numintable])

    sleep(2)
    quest = input(emoji.emojize(f'\n:robot:: \033[31mEai? O número que você pensou está na Tabela {table+1}? [S/N] \033[m '))
    if quest in 'Ss':
        if table == 0:
            num = 2**table
        else:
            num += (2**table)
print(emoji.emojize(':robot::\033[31m Bem...\033[m'))
sleep(2)
print(emoji.emojize(f':robot::\033[31m O número que você pensou foi...'), end=' ')
sleep(2)
print(f'{num}!!!')



