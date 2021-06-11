# https://codeforces.com/problemset/problem/520/B

n, m = map(int, input().split())
ans = 0

if n > m:
    ans = n-m
else:
    while n < m:
        if m%2 == 0:
            m //= 2
        else:
            m += 1
        ans += 1
    ans = abs(ans+n-m) 
print(ans)