import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        N = int(sys.argv[1])
        i  = 1
        while i<=N:
            evens = 2*i
            print(evens)
            evens -= 2
            while evens>0:
                print(evens)
                evens-=2
            i+=1
