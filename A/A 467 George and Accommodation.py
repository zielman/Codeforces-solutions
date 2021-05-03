# https://codeforces.com/problemset/problem/467/A

n = int(input())
rooms = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for room in rooms:
    if room[1] - room[0] >= 2:
        ans += 1

print(ans)