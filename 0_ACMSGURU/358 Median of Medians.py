# https://codeforces.com/problemsets/acmsguru/problem/99999/358

a = [sorted(list(map(int, input().split()))) for _ in range(3)]
b = sorted([i[1] for i in a])
print(b[1])