# https://codeforces.com/problemset/problem/266/A

def main():
    n = int(input())
    s = input()

    ans = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()