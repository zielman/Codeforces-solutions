# https://codeforces.com/problemset/problem/579/A

import math

def main():
    x = int(input())

    s = 1
    while x % (2 ** math.floor(math.log2(x))) != 0:
        x -= 2 ** math.floor(math.log2(x))
        s += 1
    
    print(s)

if __name__ == '__main__':
    main()