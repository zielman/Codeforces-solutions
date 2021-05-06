# https://codeforces.com/problemset/problem/977/B

n = int(input())
s = input()
d = {}

for i in range(n-1):
    two_gram = f"{s[i]}{s[i+1]}"
    
    if two_gram in d:
        d[two_gram] += 1
    else:
        d[two_gram] = 1
    
print(max(d, key=d.get))