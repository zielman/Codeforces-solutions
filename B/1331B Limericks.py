# https://codeforces.com/problemset/problem/1331/B

def main():
    a = int(input())
    d = 2
    while a % d != 0:
        d += 1
    print(f"{d}{a//d}")

if __name__ == '__main__':
    main()