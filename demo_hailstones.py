n = input('Starting number:')
n = int(n)
ls = []
ls.append(n)
while not n == 1:
    if n % 2 == 0:
        n = int(n / 2)
        ls.append(n)

    elif n % 2 == 1:
        n = 3 * n + 1
        ls.append(n)
print(ls)
