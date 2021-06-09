# https://codeforces.com/problemset/problem/500/A

n, t = map(int, input().split())
arr = list(map(int, input().split()))

i = 0
while i+1 < t:
    i += arr[i]

print('YES' if i+1 == t else 'NO')