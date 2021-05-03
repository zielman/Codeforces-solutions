# https://codeforces.com/problemset/problem/677/A

n, h = map(int, input().split())
nh = list(map(int, input().split()))
min_width = 0

for i in range(n):
    if nh[i] <= h:
        min_width += 1
    else:
        min_width += 2

print(min_width)