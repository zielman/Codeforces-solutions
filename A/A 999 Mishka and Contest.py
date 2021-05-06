# https://codeforces.com/problemset/problem/problem/999/A

n, k = map(int, input().split())
arr = list(map(int, input().split()))

r, l, p = 0, -1, 0

while p < n:
    if arr[r] <= k or arr[l] <= k:
        if arr[r] <= k:
            r += 1
        else:
            l -= 1    
        p += 1
    else:
        break

print(p)