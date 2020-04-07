while True:
    num = input('Integer:')
    num = int(num)
    if num == 0:
        break
    if num in range(20, 201) and num % 2 == 0 or num < 0 and num % 2 == 1:
        print("{} passes the test!".format(num))
    else:
        print("{} fails the test :(".format(num))
