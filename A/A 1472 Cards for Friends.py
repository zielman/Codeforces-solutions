# https://codeforces.com/problemset/problem/1472/A

t = int(input())
cases = [list(map(int, input().split())) for _ in range(t)]

for case in cases:
    w, h, n, ans = case[0], case[1], case[2], 1

    while w%2 == 0:
        w //= 2
        ans *= 2

    while h%2 == 0:
        h //= 2
        ans *= 2

    print('YES' if ans >= n else 'NO')