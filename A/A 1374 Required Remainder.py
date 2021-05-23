# https://codeforces.com/problemset/problem/1374/A

t = int(input())
cases = [[int(i) for i in input().split()] for i in range (t)]

for case in cases:
    x, y, n = case[0], case[1], case[2]
    print(n-n%x+y if n%x >= y else n-n%x+(y-x))