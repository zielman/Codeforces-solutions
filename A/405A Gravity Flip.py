# https://codeforces.com/problemset/problem/405/A

def main():
    n = int(input())
    col = [int(i) for i in input().split()]
    col.sort()

    print(' '.join(str(i) for i in col))

if __name__ == '__main__':
    main()