# https://codeforces.com/problemset/problem/1350/A

t = int(input())
cases = [tuple(map(int, input().split())) for _ in range(t)]

for case in cases:
    n, m = map(int, case)

    if n == 1 or m == 1:
        print('YES')
    elif n == 2 and m == 2:
        print('YES')
    else:
        print('NO')