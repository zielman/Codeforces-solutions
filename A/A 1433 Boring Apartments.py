# https://codeforces.com/problemset/problem/1433/A

t = int(input())
cases = [input() for _ in range(t)]

for case in cases:
    clicks = 10 * (int(case[0])-1)
    for i in range(1, 5):
        if i == len(case):
            clicks += i
            break
        else:
            clicks += i

    print(clicks)