def exists(ls, elem):
    i = 0
    flag = False
    while i < len(ls):
        if ls[i] == elem:
            return True
        i += 1
    return False


names = ['a', 'b', 'c']
print(exists(names,'a'))