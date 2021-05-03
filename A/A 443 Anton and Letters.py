# https://codeforces.com/problemset/problem/443/A

s = input()
r = "}{, "

for char in r:
    s = s.replace(char, '')

print(len(set([c for c in s])))