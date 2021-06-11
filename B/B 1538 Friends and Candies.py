# https://codeforces.com/problemset/problem/1538/B

t = int(input())
cases = [(int(input()), list(map(int, input().split()))) for _ in range(t)]

for case in cases:
    n, arr = case[0], case[1]
    avg = sum(arr)/n 
    
    if avg%1 != 0:
        print('-1')
    else:
        if n == 1 or n == arr.count(arr[0]):
            print('0')
        else:
            print(len([x for x in arr if x > avg]))