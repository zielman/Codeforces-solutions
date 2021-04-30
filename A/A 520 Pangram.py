# https://codeforces.com/problemset/problem/520/A

def main():
    n = int(input())
    s = input()

    alphabet = [chr(i) for i in range(65, 91)] # all upper

    for char in s.upper():
        if char in alphabet:
            alphabet.remove(char)

    if len(alphabet) == 0:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()