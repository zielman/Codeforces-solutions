# https://codeforces.com/problemset/problem/894/A

s, ans = [char for char in input() if char == 'Q' or char == 'A'], 0

for idx, char in enumerate(s):
    if char == 'Q':
        for i in range(idx+1, len(s)):
            if s[i] == 'A':
                ans += s[i+1:len(s)].count('Q')

print(ans)