# https://codeforces.com/problemset/problem/268/A

n = int(input())
uni = [list(map(int, input().split())) for _ in range(n)]

hu = [uni[i][0] for i in range(n)]
gu = [uni[i][1] for i in range(n)]

ans = 0
for u in hu:
    if u in gu:
        ans += gu.count(u)

print(ans)