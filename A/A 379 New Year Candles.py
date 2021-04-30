# https://codeforces.com/problemset/problem/379/A

def main():
    a, b = map(int, input().split())

    c = 0
    ans = 0
    while a > 0:
        ans += 1
        a -= 1
        c += 1
        if c == b:
            a += 1
            c = 0
    print(ans)

if __name__ == '__main__':
    main()