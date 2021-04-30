# https://codeforces.com/problemset/problem/144/A

def main():
    n = int(input())
    sh = [int(i) for i in input().split()]

    sh_max = sh.index(max(sh))
    sh_min = max(idx for idx, val in enumerate(sh) if val == min(sh))

    if sh_max < sh_min:
        print(sh_max + n - sh_min - 1)
    else:
        print(sh_max + n - sh_min - 2)

if __name__ == '__main__':
    main()