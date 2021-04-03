# https://codeforces.com/problemset/problem/1504/A

def isPalindrome(x):
        if x == x[::-1]:
            return True
        else:
            return False

def alla(string):
    for i in range(len(string)):
        if string[i] != 'a':
            return False
    return True

def main():
    
    t = int(input())

    strings = []

    for i in range(t):
        strings.append(input())

    for string in strings:
        if alla(string):
            print('NO')
        elif isPalindrome(f"a{string}") == False:
            print('YES')
            print(f"a{string}")            
        elif isPalindrome(f"{string}a") == False:
            print('YES')
            print(f"{string}a")
            
if __name__ == '__main__':
    main()