import random
import math


def in_circle(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    return distance < 2


i = 0
how_many_in = 0
test_num = 10000000
while i < test_num:
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    if in_circle(x, y):
        how_many_in += 1
    i += 1
area_circle = (how_many_in / test_num) * 16
pi = area_circle / 4
print(pi)
