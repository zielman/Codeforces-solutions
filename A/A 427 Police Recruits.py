# https://codeforces.com/problemset/problem/427/A


n = int(input())
events = [int(i) for i in input().split()]

crimes_untreated = 0
officers = 0

for e in events:
    if e == -1 and officers == 0:
        crimes_untreated += 1
    elif e == -1 and officers != 0:
        officers -= 1
    else:
        officers += e

print(crimes_untreated)