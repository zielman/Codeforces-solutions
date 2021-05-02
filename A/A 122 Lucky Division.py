# https://codeforces.com/problemset/problem/122/A

def if_lucky_number(x):
        for char in [char for char in x]:
            if int(char) == 4 or int(char) == 7:
                continue
            else:
                return False
        return True

def if_almost_lucky_number(x):
    lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 477, 474, 477, 744, 747, 777]
    for number in lucky_numbers:
        if int(x) % number == 0:
            return True
        else:
            continue
    else:
        return False
        
inp = input()

if if_lucky_number(inp) or if_almost_lucky_number(inp):
    print('YES')
else:
    print('NO')