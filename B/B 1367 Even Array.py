# https://codeforces.com/problemset/problem/1367/B

t = int(input())
cases = [[int(input()), list(map(int, input().split()))] for _ in range(t)]

for case in cases:
    n = case[0]
    arr = case[1]

    even, odd = 0, 0
    for i in range(0, n, 2):
        if arr[i] % 2 == 1:
            odd += 1
    for j in range(1, n, 2):
        if arr[j] % 2 == 0:
            even += 1
    
    if even == odd:
        print(even)
    else:
        print(-1)