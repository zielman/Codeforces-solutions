# https://codeforces.com/problemsets/acmsguru/problem/99999/486

x, y = input(), input()

b, c = 0, 0
for i in range(4):
    if x[i] == y[i]:
        b += 1
    if x[i] in y:
        c += 1

print(b, c-b)