# https://codeforces.com/problemset/problem/1352/C

t = int(input())
cases = [list(map(int, input().split())) for _ in range(t)]

for case in cases:
    print(case[1]+((case[1]-1)//(case[0]-1)))