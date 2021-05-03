# https://codeforces.com/problemset/problem/379/A

a, b = map(int, input().split())
c, ans = 0, 0

while a > 0:
    ans += 1
    a -= 1
    c += 1
    if c == b:
        a += 1
        c = 0
print(ans)