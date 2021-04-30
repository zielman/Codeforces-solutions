# https://codeforces.com/problemset/problem/723/A

def main():
    x = sorted([int(i) for i in input().split()])

    print((x[1] - x[0]) + (x[2] - x[1]))    

if __name__ == '__main__':
    main()