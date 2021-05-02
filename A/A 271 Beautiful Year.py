# https://codeforces.com/problemset/problem/271/A

y = int(input())
t = y + 1

while True:
    if len(set(char for char in str(t))) == 4:
        print(t)
        break
    else:
        t += 1 