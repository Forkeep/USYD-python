import sys

file_name = sys.argv[1]
file_name_ls = file_name.split('.')
pre_file_name = file_name_ls[0]
f1 = open(file_name, 'r')
f2 = open(pre_file_name + '-sorted.txt', 'w')

lines_ls = f1.readlines()

lines_ls.sort()
i = 0
while True:
    f2.write(lines_ls[i])
    i += 1
    if i == len(lines_ls):
        break
