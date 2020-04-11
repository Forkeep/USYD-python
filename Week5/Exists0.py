def exists(ls, elem):
    i = 0
    flag = False
    while i < len(ls):
        if ls[i] == elem:
            flag = True
        i += 1
    return flag


names = ['a', 'b', 'c']
print(exists(names,123))