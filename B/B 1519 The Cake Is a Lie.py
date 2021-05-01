# https://codeforces.com/problemset/problem/1519/B

t = int(input())
cases = [list(map(int, input().split())) for _ in range(t)]

for case in cases:
    if (case[0]-1) + (case[0] * (case[1]-1)) == case[2]:
        print('YES')
    else:
        print('NO')