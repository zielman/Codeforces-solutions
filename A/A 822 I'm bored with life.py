# https://codeforces.com/problemset/problem/822/A
import math

a, b = map(int, input().split())

i, x = 2, min(a,b)
while x < math.factorial(min(a,b)):
    x *= i
    i += 1

print(x)