def minimum(ls):
    i = 0
    min = 0
    while True:
        if i >= len(ls):
            break
        if ls[i]<ls[min]:
            min = i
        i+=1
    return ls[min]
#
# print(minimum([1, 2, 3, 4, 5])) # Prints: 1
# print(minimum([-1, -2, -3, -4, -5])) # Prints: -5
# print(minimum([2, 4, 1000000, -2000000, 1])) # Prints: -2000000#


