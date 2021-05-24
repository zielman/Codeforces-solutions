# https://codeforces.com/problemset/problem/1409/A

t = int(input())
cases = [list(map(int, input().split())) for _ in range(t)]

for case in cases:
    a, b = case[0], case[1]
    if (a-b) % 10 == 0:
        print(abs(a-b)//10)
    else:
        print(abs(a-b)//10 + 1)