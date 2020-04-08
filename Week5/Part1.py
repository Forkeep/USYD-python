def my_sum(ls):  # Fill this in...
    i = 0
    sum = 0
    while True:
        if i>=len(ls):
            break
        sum += ls[i]
        i+=1
    return sum




list_of_nums = [1, 2, 3, 4, 5]  # Should print: 15
print(my_sum(list_of_nums))
list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Should print: 55
print(my_sum(list_of_nums))
