# https://codeforces.com/problemset/problem/155/A

n = int(input())
p = list(map(int, input().split()))

maxP, minP, a = p[0], p[0], 0

for i in range(1, n):
    if p[i] > maxP:
        a += 1
        maxP = p[i]
    elif p[i] < minP:
        a += 1  
        minP = p[i]  

print(a)