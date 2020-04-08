import random
import math


def in_circle(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    return distance < 1

i=0
how_many_in =0
test_num = 10
print(type(test_num))
while i<test_num:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if in_circle(x,y):
        how_many_in+=1
    i+=1
area_circle = (how_many_in/test_num)*4

pi = area_circle

print(pi)



