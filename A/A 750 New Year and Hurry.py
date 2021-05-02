# https://codeforces.com/problemset/problem/750/A

n, k = map(int, input().split())

problems, time = 0, 0

for i in range(1, n+1):
    if time + (i*5) <= 240-k:
        time += i*5
        problems += 1
    else:
        break

print(problems)