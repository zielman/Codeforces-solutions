# https://codeforces.com/problemset/problem/486/A

n = int(input())

print(int(n / 2) if n % 2 == 0 else int((n + 1) / (-2)))