# https://codeforces.com/problemset/problem/80/A

def PrimesBeetween(a: int, b: int) -> list:
    out = list()
    sieve = [True] * (b+1)
    for p in range(2, b+1):
        if (sieve[p] and sieve[p]%2==1):
            if p > a:
                out.append(p)
            for i in range(p, b+1, p):
                sieve[i] = False
    return out

def main():
    n, m = map(int, input().split())

    arr = PrimesBeetween(n, m)
    
    if len(arr) == 1 and arr[0] == m:
        print('YES')
    else:
        print('NO')

if __name__=='__main__':
    main()