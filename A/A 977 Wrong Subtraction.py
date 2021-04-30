# https://codeforces.com/problemset/problem/977/A

def main():
    n, k = map(int, input().split())

    i = 0
    while i < k:
        if n % 10 != 0:
            n -= 1
            i += 1
        elif n % 10 == 0:
            n /= 10
            i += 1

    print(int(n))

if __name__ == '__main__':
    main()