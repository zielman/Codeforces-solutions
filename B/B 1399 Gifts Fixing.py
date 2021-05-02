# https://codeforces.com/problemset/problem/1399/B

t = int(input())
cases = [[int(input()), list(map(int, input().split())), list(map(int, input().split()))] for _ in range(t)]

for case in cases:
    n, arr, brr = case[0], [i - min(case[1]) for i in case[1]], [i - min(case[2]) for i in case[2]]

    moves = 0
    for i in range(n):
        moves += min(arr[i], brr[i]) + abs(arr[i] - brr[i])
    
    print(moves)