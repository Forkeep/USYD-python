import sys
file = sys.argv[1]
target = sys.argv[2]
replacement = sys.argv[3]

f = open(file,'r')
lines_ls = f.readlines()
i = 0
while True:
    lines_ls[i] =  lines_ls[i].replace(target,replacement)
    i+=1
    if i == len(lines_ls):
        break
print(lines_ls)
f.close()

f = open(file,'w')
i = 0
while True:
    f.write(lines_ls[i])
    i+=1
    if i==len(lines_ls):
        break
