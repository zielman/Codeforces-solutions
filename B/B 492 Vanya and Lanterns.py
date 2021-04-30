# https://codeforces.com/problemset/problem/492/B

n, l = map(int, input().split()) # n = number of lanterns, l = length of the street
nList = sorted(list(map(int, input().split())))

d = max(nList[0], l - nList[-1])

for i in range(n - 1):
    d = max(d, (nList[i + 1] - nList[i]) / 2)

print(d)