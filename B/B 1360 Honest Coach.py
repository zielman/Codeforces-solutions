# https://codeforces.com/problemset/problem/1360/B

t = int(input())
cases = [[int(input()), sorted(list(map(int, input().split())))] for _ in range(t)]

for case in cases:
    n = case[0]
    arr = case[1]

    AB = None
    for i in range(n-1):
        if AB != None:
            AB = min(AB, arr[i+1] - arr[i])
        else:
            AB = arr[i+1] - arr[i]

    print(AB)