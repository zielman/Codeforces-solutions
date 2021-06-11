# https://codeforces.com/problemset/problem/702/A

n, arr = int(input()), list(map(int, input().split()))

ans, temp = 1, 1

for i in range(n-1):
    if arr[i] < arr[i+1]:
        temp += 1
        ans = max(ans,temp)
    else:
        temp = 1

print(ans)