# https://codeforces.com/problemset/problem/271/A

def split(string):
    return [char for char in string]

def is_distinct(year):
        if len(set(split(str(year)))) == 4:
            return True
        else:
            return False

def main():
    y = int(input())
    next_y = y + 1
   
    while True:
        if is_distinct(next_y):
            print(next_y)
            break
        else:
            next_y += 1 
   
if __name__ == '__main__':
    main()