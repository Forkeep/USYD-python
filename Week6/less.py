import sys

file_name = ''
if len(sys.argv) == 2:
    file_name = sys.argv[1]


f = open(file_name, 'r')

line_ls = f.readlines()

print(line_ls)
while True:
    line = f.readline()
    print(line, end = ' ')
    mode = input('')
    if not mode:
        continue
    if mode == 'q':
        break
