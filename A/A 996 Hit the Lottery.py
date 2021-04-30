# https://codeforces.com/problemset/problem/996/A

def main():
    n = int(input())
    d = [1, 5, 10, 20, 100]

    ans = 0
    for i in d[::-1]:
        ans += n // i
        n = n % i

    print(ans)

if __name__ == '__main__':
    main()