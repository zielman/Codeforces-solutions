# https://codeforces.com/problemsets/acmsguru/problem/99999/115

n, m = map(int, input().split())
mth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if m > 12:
    print('Impossible')
elif n > mth[m-1]:
    print('Impossible')
else:
    d = (sum(mth[:-13+m])+n) % 7
    print(7 if d == 0 else d)