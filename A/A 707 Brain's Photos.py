# https://codeforces.com/problemset/problem/707/A

row, col = map(int, input().split())
rows = [list(map(str, input().split())) for _ in range(row)]

for row in rows:
    for i in range(col):
        if row[i] == 'C' or row[i] == 'M' or row[i] == 'Y':
            print('#Color')
            break
    else:
        continue
    break
else:
    print('#Black&White')