# https://codeforces.com/problemset/problem/1514/A

import math

def isNotPerfectSquare(num: int) -> bool:
    return num != math.isqrt(num) ** 2

t = int(input())
cases = [[int(input()) , list(map(int, input().split()))] for _ in range(t)]

for case in cases:
    for i in range(case[0]):
        if isNotPerfectSquare(case[1][i]):
            print('YES')
            break
    else:
        print('NO')