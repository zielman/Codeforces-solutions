# https://codeforces.com/problemsets/acmsguru/problem/99999/105

N = int(input())

if N%3 == 2:
    print(N//3*2+1)
else:
    print(N//3*2)