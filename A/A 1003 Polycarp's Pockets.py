# https://codeforces.com/problemset/problem/problem/1003/A

n, arr = int(input()), list(map(int, input().split()))
d = {}

for num in arr:
    if num not in d:
        d[num] = 1
    else:
        d[num] += 1

print(max(d.values()))