# https://codeforces.com/problemset/problem/520/A

n, s = int(input()), input()

alphabet = [chr(i) for i in range(65, 91)] # all upper

for char in s.upper():
    if char in alphabet:
        alphabet.remove(char)

print('YES' if len(alphabet) == 0 else 'NO')