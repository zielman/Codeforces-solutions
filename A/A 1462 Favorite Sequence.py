# https://codeforces.com/problemset/problem/1462/A

t = int(input())
cases = [(int(input()), list(map(int, input().split()))) for _ in range(t)]

for case in cases:
    n, arr, ans = case[0], case[1], []
    i, j = 0, 0
    while j < n:
        ans.append(arr[i])
        j += 1
        if i >= 0:
            i += 1
            i *= -1
        else:
            i *= -1
    print(' '.join(str(i) for i in ans))