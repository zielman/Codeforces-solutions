# https://codeforces.com/problemset/problem/1529/A

t = int(input())
cases = [(int(input()), list(map(int, input().split()))) for _ in range(t)]

for case in cases:
    print(case[0] - case[1].count(min(case[1])))




