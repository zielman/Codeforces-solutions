# https://codeforces.com/problemset/problem/492/A

n = int(input()) 
blocks, level, total = 1, 1, 1

while total <= n:
    level += 1
    blocks += level
    total += blocks

print(level-1)