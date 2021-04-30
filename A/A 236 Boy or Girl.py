# https://codeforces.com/problemset/problem/236/A

inp = input()

inp_list = [char for char in inp]
inp_set = set(inp_list)

if len(inp_set) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')