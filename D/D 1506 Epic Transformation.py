# https://codeforces.com/contest/1506/problem/D

for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    i = (n // 2) - 1
    j = n - 1
    ans = 0
    while i >= 0 and j >= n // 2:
        if l[i] != l[j]:
            ans += 2
        i -= 1
        j -= 1
    print(n - ans)