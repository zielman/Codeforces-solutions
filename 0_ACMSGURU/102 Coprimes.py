# https://codeforces.com/problemsets/acmsguru/problem/99999/102

import math

N = int(input())
cpN = 0
for i in range(1, N+1):
    if math.gcd(i, N) == 1:
        cpN += 1
print(cpN)