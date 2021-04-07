# https://codeforces.com/problemset/problem/337/A

def main():
    n, m = map(int, input().split())
    p = [int(p) for p in input().split()]
    p.sort()
    
    t = None
    if n == m:
        t = p[-1] - p[0]
    else:   
        for i in range(m - n + 1):
            if t == None:
                t = p[i + n - 1] - p[i]
            else:
                t = min(t, p[i + n - 1] - p[i])
            
    print(t)

if __name__ == '__main__':
    main()