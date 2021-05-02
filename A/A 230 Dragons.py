# https://codeforces.com/problemset/problem/230/A

s, n = map(int, input().split())
dragons = sorted([[int(j) for j in input().split()] for i in range(n)], key=lambda x: x[0])

for d in dragons:
    if s > d[0]:
        s += d[1]
    else:
        print('NO')
        break
else:
    print('YES')