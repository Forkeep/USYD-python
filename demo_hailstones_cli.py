import sys

n = sys.argv[1]
n = int(n)
all_ls = []
for i in range(1, n + 1):
    ls = []
    ls.append(i)
    while not i == 1:
        if i % 2 == 0:
            i = int(i / 2)
            ls.append(i)

        elif i % 2 == 1:
            i = 3 * i + 1
            ls.append(i)
    all_ls.append(ls)

max_len = 0
max_ls = []
for item in all_ls:
    if len(item)>max_len:
        max_len = len(item)
        max_ls = item

print(max_ls)

