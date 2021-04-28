# https://codeforces.com/problemset/problem/32/B

def main():
    code = input()

    code = code.replace('--', '2')
    code = code.replace('-.', '1')
    code = code.replace('.', '0')

    print(code)

if __name__ == '__main__':
    main()