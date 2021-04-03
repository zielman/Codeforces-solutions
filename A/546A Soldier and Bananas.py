# https://codeforces.com/problemset/problem/546/A

def main():
    
    k, n, w = map(int, input().split())

    n_needed = 0

    for i in range(1, w + 1 ):
        n_needed += i * k

    if n_needed <= n:
        print(0)
    else:
        print(n_needed - n)

if __name__ == '__main__':
    main()