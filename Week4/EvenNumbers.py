import sys

if len(sys.argv) == 2:
    first_n = int(sys.argv[1])
    i = 1
    while i < first_n + 1:
        evens = 2 * i
        print(evens)
        i += 1

if len(sys.argv) == 3:
    first_n = int(sys.argv[1])
    less_n = int(sys.argv[2])
    i = less_n+1
    while i < first_n + less_n + 1:
        evens = 2*i
        print(evens)
        i += 1
