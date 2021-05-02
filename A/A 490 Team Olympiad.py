# https://codeforces.com/problemset/problem/490/A

n = int(input())
arr = list(map(int, input().split()))

pro, math, pe = [i for i, x in enumerate(arr) if x == 1], [i for i, x in enumerate(arr) if x == 2], [i for i, x in enumerate(arr) if x == 3]
t = min(len(pro), len(math), len(pe))

print(t)
for i in range(t):
    print(pro[i]+1, math[i]+1, pe[i]+1)