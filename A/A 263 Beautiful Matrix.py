# https://codeforces.com/problemset/problem/263/A

matrix = [list(map(int, input().split())) for _ in range(5)]

r, c = 0, 0

for row in matrix:
    r += 1
    if 1 in row:
        c = row.index(1) + 1
        break

print(abs(3 - c) + abs(3 - r))