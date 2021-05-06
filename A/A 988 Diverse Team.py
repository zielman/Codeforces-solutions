# https://codeforces.com/problemset/problem/problem/988/A

n, k = map(int, input().split())
arr = list(map(int, input().split()))

brr = list(set(arr))

if len(brr) >= k:
    ans = []
    i = 0
    while i < k:
        ans.append(arr.index(brr[i]))
        i += 1
    print('YES')
    print(' '.join(str(i+1) for i in ans))
else:
    print('NO')