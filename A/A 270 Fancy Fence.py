# https://codeforces.com/problemset/problem/270/A

t = int(input())
cases = [int(input()) for _ in range(t)]

for a in cases:
    print('YES' if (360/(180-a))%1==0 else 'NO')