# https://codeforces.com/problemset/problem/1371/A

t = int(input())
cases = [int(input()) for _ in range(t)]

for n in cases:
    print((n-1)//2+1)