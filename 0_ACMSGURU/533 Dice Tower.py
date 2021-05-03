# https://codeforces.com/problemsets/acmsguru/problem/99999/533

n = int(input())

if n < 30:
    if n == 21:
        print(1)
    else:
        print(-1)
else:
    for i in range(2, 13):
        if ((n-i) / 7) % 2 == 0:
            print((n-i) // 14)
            break
    else:
        print(-1)