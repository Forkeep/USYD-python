def my_string_concatenation(ls): # Fill this in...
    i = 0
    str_result = ''
    while True:
        if i>=len(ls):
            break
        str_result+=ls[i]
        i+=1
    return str_result

list_of_strings = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']
# Should print: abcdefghijklmnopqrstuvwxyz
print(my_string_concatenation(list_of_strings))
