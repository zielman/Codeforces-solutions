# https://codeforces.com/problemset/problem/228/A

colors = list(map(int, input().split()))
col_set = set(colors)

print(len(colors)- len(col_set))