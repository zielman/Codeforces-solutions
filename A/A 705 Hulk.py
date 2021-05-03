# https://codeforces.com/problemset/problem/705/A

n = int(input())
ans = ['I hate']

if n == 1:
    pass
else:
    for i in range(2, n + 1):
        if i % 2 == 0:
            ans.append(' that I love')
        else:
            ans.append(' that I hate')
ans.append(' it')

print(''.join(ans))