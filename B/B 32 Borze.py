# https://codeforces.com/problemset/problem/32/B

code = input()

code = code.replace('--', '2')
code = code.replace('-.', '1')
code = code.replace('.', '0')

print(code)