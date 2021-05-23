# https://codeforces.com/problemset/problem/1374/A

t = int(input())
cases = [list(map(int, input().split())) for _ in range(t)]

for case in cases:
    x, y, n = case[0], case[1], case[2]
    print(n-n%x+y if n%x >= y else n-n%x+(y-x))