# https://codeforces.com/problemset/problem/1294/A

t = int(input())
cases = [list(map(int, input().split())) for _ in range(t)]

for case in cases:
    min_eq = sum(max(case[:-1])-c for c in case[:-1])
    if case[3] >= min_eq and (case[3]-min_eq) % 3 == 0:
        print('YES')
    else:
        print("NO")