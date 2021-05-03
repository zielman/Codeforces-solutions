# https://codeforces.com/problemset/problem/460/A

n, m = map(int, input().split())

print(n + (n - 1) // (m - 1))