# https://codeforces.com/problemset/problem/231/A

n = int(input())
views = [list(map(int, input().split())) for _ in range(n)]

solutions = 0
for p in views:
    if sum(p) >= 2:
        solutions += 1

print(solutions)