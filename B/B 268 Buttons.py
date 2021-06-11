# https://codeforces.com/problemset/problem/268/B

n = int(input())
i, j, ans = 1, n-1, n

while j:
    ans += i*j
    i += 1
    j -= 1

print(ans)