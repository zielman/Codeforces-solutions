# https://codeforces.com/problemset/problem/318/A

def main():
    n, k = map(int, input().split())

    if k <= (n + 1) / 2:
        print(k * 2 - 1)
    else:
        print(int((k - (n+1) // 2 ) * 2))

if __name__ == '__main__':
    main()