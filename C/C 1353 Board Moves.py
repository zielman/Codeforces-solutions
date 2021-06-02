# https://codeforces.com/problemset/problem/1353/C

t = int(input())
cases = [int(input()) for _ in range(t)]

for n in cases:
    s = 0
    for i in range(1, n+1, 2):
        s += 4*(i-1)*(i//2)
    print(s)