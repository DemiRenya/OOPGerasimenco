n = input('Введите число N ')
n=int (n)
if n <= 9 :
    for i in range (1, n + 1) :
        for j in range (1, i + 1) :
            print(j, end='')
        print('\n')
else: print('N больше 9')
