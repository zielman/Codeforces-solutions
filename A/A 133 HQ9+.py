# https://codeforces.com/problemset/problem/133/A

inp = input()
instructions = ['H', 'Q', '9']

for char in instructions:
    if char in inp:
        print("YES")
        break
else:
    print("NO")