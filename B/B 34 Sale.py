# https://codeforces.com/problemset/problem/34/B

n, m = map(int, input().split())
prices = sorted(map(int, input().split()))

money = 0
for i in range(m):
    if prices[i] < 0:
        money -= prices[i]
    else:
        break

print(money)