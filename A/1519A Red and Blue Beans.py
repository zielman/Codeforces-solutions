# https://codeforces.com/problemset/problem/1519/A

t = int(input())
cases= [list(map(int, input().split())) for _ in range(t)]

for case in cases:
    if  abs(case[0] - case[1]) / min(case[0], case[1]) <= case[2]:
        print('YES')
    else:
        print('NO')