# https://codeforces.com/problemset/problem/50/A

def main():

    m, n = map(int, input().split())

    if m % 2 == 0:
        d = m / 2 * n
        print(int(d))
    elif m % 2 == 1:
        d = (m - 1) / 2 * n
        if n % 2 == 0:
            r = n / 2
            print(int(d + r))
        elif n % 2 == 1:
            r = (n - 1) / 2
            print(int(d + r))
    else:
        print(0)

if __name__ == '__main__':
    main()