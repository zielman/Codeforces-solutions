# https://codeforces.com/problemset/problem/122/A

def split(word):
    return [char for char in word]

def if_lucky_number(x):
        for char in split(x):
            if int(char) == 4 or int(char) == 7:
                continue
            else:
                return False
                break
        return True

def if_almost_lucky_number(x):
    
    lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 477, 474, 477, 744, 747, 777]
    
    for number in lucky_numbers:
        if int(x) % number == 0:
            return True
            break
        else:
            continue
    else:
        return False
        
def main():

    inp = input()

    if if_lucky_number(inp) or if_almost_lucky_number(inp):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()