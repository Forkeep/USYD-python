f = open('food.txt', 'r')

while True:
    line = f.readline()
    if line =='':
        print(line+'line shizheli')
        break
    else:
        arr = line.split(' ')
        print(arr[0])
        print(arr[1])
f.close()
