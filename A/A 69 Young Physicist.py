# https://codeforces.com/problemset/problem/69/A

n = int(input())
coordinates = [list(map(int, input().split())) for _ in range(n)]

x, y, z = 0, 0, 0

for c in coordinates:
    x += c[0]
    y += c[1]
    z += c[2]

if x == 0 and y == 0 and z ==0:
    print('YES')
else:
    print('NO')