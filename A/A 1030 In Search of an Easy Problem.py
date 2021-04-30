# https://codeforces.com/problemset/problem/1030/A

def main():
    n = int(input())
    o = list(map(int, input().split()))

    if o.count(1) != 0:
        print('HARD')
    else:
        print('EASY')

if __name__ == '__main__':
    main()