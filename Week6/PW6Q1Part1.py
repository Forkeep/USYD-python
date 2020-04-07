f = open('numbers.txt','a')
i=0
while True:
    i+=1
    f.write('{}\n'.format(i))
    if  i==10:
        break

f.close()
