# https://codeforces.com/problemset/problem/148/A

def main():
    klmn = [int(input()) for i in range(4)]
    d = int(input())
    klmn = [i for i in klmn if i <= d]
    
    if 1 in klmn:
        print(d)
    elif len(klmn) == 0:
        print(0)
    else:
        sieve = [True] * (d)
        i = 0
        while i < 4:
            if sieve[klmn[i]-1] == True:
                for j in range(klmn[i]-1, d, klmn[i]):
                    sieve[j] = False
            i += 1
        
        print(sieve[1:].count(False))

if __name__ == '__main__':
    main()