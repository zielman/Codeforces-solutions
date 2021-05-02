# https://codeforces.com/problemset/problem/116/A

n = int(input())
stops = [list(map(int, input().split())) for _ in range(n)]

p, peak_p = 0, 0

for stop in stops:
    p -= stop[0]
    p += stop[1]
    peak_p = max(p, peak_p)

print(peak_p)