# https://codeforces.com/problemset/problem/1335/A


t = int(input())
cases = [int(input()) for c in range(t)]

for c in cases:
    if c <= 2:
        print(0)
    else:
        if c % 2 == 0:
            print(c//2 - 1)
        else:
            print(c//2)