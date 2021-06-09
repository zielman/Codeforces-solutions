# https://codeforces.com/problemset/problem/1335/D

t = int(input())
cases = [[input() for row in range(9)] for _ in range(t)]

for sudoku in cases:
    for row in sudoku:
        print(row.replace('1', '2'))