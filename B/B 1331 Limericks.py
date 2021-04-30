# https://codeforces.com/problemset/problem/1331/B

a = int(input())
d = 2
while a % d != 0:
    d += 1
    
print(f"{d}{a//d}")