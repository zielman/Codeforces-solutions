# https://codeforces.com/problemset/problem/1328/A

t = int(input())
cases = [list(map(int, input().split())) for _ in range(t)]

for case in cases:
    if case[0] % case[1] == 0:
        steps = 0
    else:
        steps = case[1] - (case[0] % case[1])
    print(steps)