# https://codeforces.com/problemset/problem/978/B

n, s = int(input()), input()
in_row, delate = 0, 0

for i in range(n-1):
    if s[i] == 'x' and s[i+1] == 'x' and in_row < 2:
        in_row = 2
    elif s[i] == 'x' and s[i+1] == 'x' and in_row >= 2:
        in_row += 1
        delate += 1
    else:
        in_row = 0

print(delate)