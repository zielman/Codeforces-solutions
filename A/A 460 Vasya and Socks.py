# https://codeforces.com/problemset/problem/460/A

def main():
    n, m = map(int, input().split())
    
    print(n + (n - 1) // (m - 1))

if __name__ == '__main__':
    main()