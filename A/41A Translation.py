# https://codeforces.com/problemset/problem/41/A

s = input()
t = input()

if t == s[::-1]:
    print('YES')
else:
    print('NO')