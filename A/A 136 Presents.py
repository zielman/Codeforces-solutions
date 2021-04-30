# https://codeforces.com/problemset/problem/136/A

def main():
    n = int(input())
    ip = list(map(int, input().split()))

    ans = [ip.index(idx + 1) + 1 for idx, p in enumerate(ip)]
    print(''.join(f"{x} " for x in ans))

if __name__ == '__main__':
    main()