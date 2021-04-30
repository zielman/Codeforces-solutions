# https://codeforces.com/problemset/problem/4/A

w = int(input())
r = w - 2

if r % 2 == 0 and r >= 2:
    print('YES')
else:
    print('NO')