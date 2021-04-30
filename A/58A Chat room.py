# https://codeforces.com/problemset/problem/58/A

s = input()
check = []

for i in range(len(s)):
    if s[i] == 'h' and s[i] not in check:
        check.append('h')
    elif s[i] == 'e' and ''.join(check) == 'h':
        check.append('e')
    elif s[i] == 'l' and ''.join(check) == 'he' or s[i] == 'l' and ''.join(check) == 'hel':
        check.append('l')
    elif s[i] == 'o' and ''.join(check) == 'hell':
        check.append('o')
    
print("YES" if ''.join(check) == 'hello' else "NO")