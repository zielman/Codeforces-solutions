# https://codeforces.com/problemset/problem/1186/A

n, m, k = map(int, input().split())

print('YES' if min(m,k)>=n else 'NO')