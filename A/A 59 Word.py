# https://codeforces.com/problemset/problem/59/A

word = input()
u, l = 0, 0

for char in word:
    if char >= 'A' and char <= 'Z':
        u += 1
    elif char >= 'a' and char <= 'z':
        l += 1

if u > l:
    print(word.upper())
else:
    print(word.lower())