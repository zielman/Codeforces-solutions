# https://codeforces.com/problemset/problem/1490/A

t = int(input())
cases = [(int(input()) , list(map(int, input().split()))) for _ in range(t)]

for case in cases:
    n, arr, ans = case[0], case[1], 0

    for i in range(len(arr)-1):
        a, b = max(arr[i], arr[i+1]), min(arr[i], arr[i+1])
        if a/b > 2:
            c = b
            while c*2 < a:
                c *= 2
                ans += 1
    print(ans)