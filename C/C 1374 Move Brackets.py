# https://codeforces.com/problemset/problem/1374/C

t = int(input())
cases = [(int(input()), input()) for _ in range(t)]

for case in cases:
    n, s, x = case[0], case[1], 0

    for char in s:
        if char =='(':
            x += 1
        else:
            if x > 0:
                x -= 1
    
    print(x)