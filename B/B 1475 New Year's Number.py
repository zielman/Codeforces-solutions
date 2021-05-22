# https://codeforces.com/problemset/problem/1475/B

t = int(input())
cases = [int(input()) for _ in range(t)]

for num in cases:
    print('YES' if num % 2020 <= num // 2020 else 'NO')