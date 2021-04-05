# https://codeforces.com/problemset/problem/41/A

def main():
    s = input()
    t = input()

    if t == s[::-1]:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()