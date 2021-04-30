# https://codeforces.com/problemset/problem/4/C

n = int(input())
db = {}

for i in range(n):
    name = input()
    if name not in db:
        print('OK')
        db[name] = 1
    else:
        print(f"{name}{db[name]}")
        db[name] += 1