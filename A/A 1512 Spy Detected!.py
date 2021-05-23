# https://codeforces.com/problemset/problem/1512/A

t = int(input())
cases = [(int(input()), list(map(int, input().split()))) for _ in range(t)]

for case in cases:
    an = case[1]
    anSet = list(set(an))
    if an.count(anSet[0]) < an.count(anSet[1]):
        print(an.index(anSet[0])+1)
    else:
        print(an.index(anSet[1])+1)