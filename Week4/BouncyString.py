import sys

if __name__ == '__main__':
    if len(sys.argv) == 4:
        word = list(sys.argv[1])
        length = len(word)
        start = int(sys.argv[2])
        N = int(sys.argv[3])
        end = N + start
        j = start
        #  构造bouncy String
        bouncy_str = []
        copy_i = 0
        while copy_i < length:
            bouncy_str.append(word[copy_i])
            copy_i += 1
        bi = length - 2
        while bi > 0:
            bouncy_str.append(word[bi])
            bi-=1
        while j < end:
            if j >= length:
                print(bouncy_str[j%len(bouncy_str)], end='')
            else:
                print(bouncy_str[j], end='')
            j += 1
