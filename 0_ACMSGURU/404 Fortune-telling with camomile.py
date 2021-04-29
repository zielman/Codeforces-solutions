# https://codeforces.com/problemsets/acmsguru/problem/99999/404

n, m = map(int, input().split())
phrases = [input() for i in range(m)]

print(phrases[n%m-1])