# https://codeforces.com/problemset/problem/1369/A

t = int(input())
cases = [int(input()) for _ in range(t)]

for case in cases:
    print('YES' if case % 4 == 0 else 'NO')