# https://codeforces.com/problemset/problem/339/B

n, m = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
last = 1
for h in arr:
    if last <= h:
        s += h - last
    else:
        s += n - last + h
    last = h
print(s)