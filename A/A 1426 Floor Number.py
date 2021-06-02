# https://codeforces.com/problemset/problem/1426/A

import math

t = int(input())
cases = [list(map(int, input().split())) for _ in range(t)]

for case in cases:
    if case[0] <= 2:
        print(1)
    else:
        print(math.ceil((case[0]-2)/case[1]+1))