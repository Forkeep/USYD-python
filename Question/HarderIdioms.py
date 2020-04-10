num_input = input("input: ")
num_ls = list(num_input)
i = len(num_ls) - 1
j = 0
base10 = 0
while i >= 0:
    base2 = int(num_ls[i])
    add_base2 =  base2 * (2 ** j)
    base10 = base10 + add_base2
    j += 1
    i -= 1
print(base10)


# 顺序计算
i = 0
while i<len(num_ls):
    pass
    i+=1

# 逆序计算
i=len(num_ls)-1
while i>=0:
    pass
    i-=1