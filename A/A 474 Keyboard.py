# https://codeforces.com/problemset/problem/474/A

shift, message = [-1 if input() == 'R' else 1], input()
keyboard = 'qwertyuiopasdfghjkl;zxcvbnm,./'

print(''.join([keyboard[keyboard.index(char)+shift[0]] for char in message]))