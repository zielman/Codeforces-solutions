# https://codeforces.com/problemset/problem/1283/A

t = int(input())
cases = [list(map(int, input().split())) for _ in range(t)]

for case in cases:
    print(((24-case[0]) * 60) - case[1])