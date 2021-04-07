# https://codeforces.com/problemset/problem/344/A

def main():
    n = int(input())
    mags = [input() for i in range(n)]

    g = 1
    if n == 1:
        pass
    else:
        for i in range(1, n):
            if mags[i - 1] != mags[i]:
                g += 1

    print(g)

if __name__ == '__main__':
    main()