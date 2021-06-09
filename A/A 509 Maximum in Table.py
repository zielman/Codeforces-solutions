# https://codeforces.com/problemset/problem/509/A

n = int(input())
arr = [1]*n

for _ in range(n-1):
    for i in range(1,n):
        arr[i] += arr[i-1]

print(arr[-1])