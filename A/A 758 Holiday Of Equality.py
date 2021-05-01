# https://codeforces.com/problemset/problem/758/A

n = int(input())
welfare = list(map(int, input().split()))

r = max(welfare)
s = 0
for c in welfare:
    s += r - c

print(s)