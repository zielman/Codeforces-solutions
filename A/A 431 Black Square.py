# https://codeforces.com/problemset/problem/431/A

a, b, c, d = map(int, input().split())
table = {'1': a, '2': b, '3': c, '4': d}

print(sum(table[char] for char in input()))