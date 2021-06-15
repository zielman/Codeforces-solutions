# https://codeforces.com/problemset/problem/584/A

n, t  = map(int, input().split())

if n == 1:
    if t < 10:
        print(t)
    else:
        print(-1)
else:
    if t < 10:
        print(str(t)+'0'*(n-1))
    else:
        print('1'+'0'*(n-1))