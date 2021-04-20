# https://codeforces.com/problemset/problem/451/A

def main():
    n, m = map(int, input().split())

    if min(n, m) % 2 == 0:
        print('Malvika')
    else:
        print('Akshat')
        
if __name__ == '__main__':
    main()