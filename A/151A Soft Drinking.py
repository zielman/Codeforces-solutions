# https://codeforces.com/problemset/problem/151/A
 
def main():
    n, k, l, c, d, p, nl, np = map(int, input().split())

    print(min(k*l//nl, c*d, p//np) // n)
    
if __name__ == '__main__':
    main()