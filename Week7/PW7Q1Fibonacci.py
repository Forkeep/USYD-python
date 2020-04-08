def fibonacci(num):
    ls = [0, 1]
    try:
        if not isinstance(num, int):
            raise TypeError('Please pass in an integer.')
        if num <= 0:
            raise ValueError('Input must be 1 or greater.')
        i = 1
        while True:
            if i == num+1:
                break
            cur = ls[i - 1] + ls[i]
            ls.append(cur)
            i += 1
        return ls[num+1]
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)

print(fibonacci(6))
