# https://codeforces.com/problemset/problem/432/A

n, k = map(int, input().split())
nList = [int(i) for i in input().split() if int(i) + k <= 5]

print(len(nList)//3)