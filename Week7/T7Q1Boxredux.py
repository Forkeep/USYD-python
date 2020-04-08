import sys

if len(sys.argv) == 2:
    num = int(sys.argv[1])
    i = 0
    while True:
        if i == num:
            break
        if i == 0 or i==num-1:
            print('+', end='')
            j = 0
            while True:
                if j == num:
                    break
                print('-', end='')
                j += 1
            print('+')
        else:
            print('|',end='')
            j = 0
            while True:
                if j==num:
                    break
                print(' ',end='')
                j+=1
            print('|')
        i += 1
else:
    print('input error!')
