# https://codeforces.com/problemset/problem/1353/B

t = int(input())
cases = [[list(map(int, input().split())), map(int, input().split()), map(int, input().split())] for _ in range(t)]

for case in cases:
    n, k = case[0][0], case[0][1]
    arr, brr = sorted(list(case[1])), sorted(list(case[2]), reverse=True)
    i, ans = 0, sum(arr)
    
    while i < k:
        if arr[i] < brr[i]:
            ans += brr[i] - arr[i]
        i += 1
        
    print(ans)