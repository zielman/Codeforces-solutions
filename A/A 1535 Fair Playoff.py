# https://codeforces.com/problemset/problem/1535/A

t = int(input())
cases = [list(map(int, input().split())) for _ in range(t)]

for case in cases:
    top = sorted(case, reverse=True)[:2]
    if max(case[0], case[1]) in top and max(case[2], case[3]) in top:
        print('YES')
    else:
        print('NO')