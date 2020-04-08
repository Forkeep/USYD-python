def integer(str):
    length = len(str)
    num_ls = list(str)
    i = length - 1
    j = 0
    num = 0
    while True:
        if i < 0:
            break
        num_int = ord(num_ls[i]) - ord('0')
        num += num_int * 10 ** j
        i -= 1
        j += 1
    return num

print(integer('234134'))
