# https://codeforces.com/problemset/problem/118/A

vowels = {"A", "O", "Y", "E", "U", "I"}

inp = input().lower()

ans = []
for i in inp:
    if i.upper() not in vowels:
        ans.append(".")
        ans.append(i)

print(''.join(ans))