# https://codeforces.com/problemset/problem/1475/A

t = int(input())
cases = [int(input()) for _ in range(t)]

for num in cases:
    s = bin(num-1)[2:]
    print('NO' if s.count('1') == len(s) else 'YES')