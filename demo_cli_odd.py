import sys

if len(sys.argv) == 2:
    if sys.argv[1] == '-a':
        n = 0
        while True:
            if n % 2 == 1:
                print(n)
            n += 1
            if n == 100:
                break
    elif sys.argv[1] == '-d':
        n = 100
        while True:
            if n % 2 == 1:
                print(n)
            n -= 1
            if n == 0:
                break
    else:
        sys.exit('Usage: python3 odds_again.py (-a | -d)')

else:
    sys.exit('Usage: python3 odds_again.py (-a | -d)')
