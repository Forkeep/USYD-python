t_num = 1 # the current triangular number to print out
step = 2 # the quantity added to `t_num`, to get the next triangular number print('Hello!')
while t_num <= 15:
    # print(t_num)
    if t_num % 2 == 0:
        print(t_num)
        pass
    elif t_num % 5 == 0:
        print(t_num)
        pass
    t_num += step
    step += 1