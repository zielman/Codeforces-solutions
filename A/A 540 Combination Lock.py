# https://codeforces.com/problemset/problem/540/A

n, x, y = int(input()), input(), input()
moves = 0

for i in range(n):
    d = max(int(x[i]), int(y[i])) - min(int(x[i]), int(y[i])) 
    if d <= 5:
        moves += d
    else:
        moves += 10 - d

print(moves)