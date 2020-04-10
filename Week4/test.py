a = [1, 2, 3]
b = []
i = 0
while i < len(a):
    b.append(a[i])
    i+=1

a[1] = 9
print(b)