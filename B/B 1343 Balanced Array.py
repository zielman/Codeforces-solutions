# https://codeforces.com/problemset/problem/1343/B

def main():
    t = int(input())
    for i in range(t):    
        n = int(input())
        if n % 4 != 0:
            print('NO')
        else:
            le = [e for e in range(2, n+1, 2)] 
            lo = [o for o in range(1, n+1, 2)]
            leSum = sum(le)
            loSum = sum(lo)
            
            while leSum > loSum:
                lo[-1] += 2 * n//4
                loSum += 2 * n//4
            if leSum == loSum:
                print('YES')
                print(' '.join([str(i) for i in le] + [str(i) for i in lo]))

if __name__ == '__main__':
    main()