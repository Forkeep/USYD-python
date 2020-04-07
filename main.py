
x=1
y=1
print(id(x), id(y)) # Same
x=5
y=5
print(id(x), id(y)) # x is different, but y is same as before
x = [1, 2, 3]
y=x
print(id(x), id(y)) # Same
# Fun fact, print() also has a memory address!
print(id(print))