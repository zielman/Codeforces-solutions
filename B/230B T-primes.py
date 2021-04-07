# https://codeforces.com/problemset/problem/230/B

def genPrimesTo(lim):
    primes = [True] * lim
    primes[0] = primes[1] = False
    for i in range(2, lim):
        if primes[i] == True:
            for j in range(i*i, lim, i):
                primes[j] = False
    return primes

def isTPrime(n, primes):
    if n == 4:
        return True
    if n < 4 or n % 2 == 0:
        return False
    sqrt_n = n**0.5
    if sqrt_n == int(sqrt_n):
        if primes[int(sqrt_n)] == True:
            return True
    return False

def main():
    n = int(input())
    numbers = [int(i) for i in input().split()]
    
    lim = 1000000
    primes = genPrimesTo(lim)
   
    for num in numbers:
        if isTPrime(num, primes):
            print('YES')
        else:
            print('NO')
 
if __name__ == '__main__':
    main()