# https://codeforces.com/problemset/problem/466/A

import math

def main():
    
    n, m, a, b = map(int, input().split())
    
    single = n * a
    multi = math.ceil(n / m) * b
    combined = (math.floor(n / m) * b) + n % m * a
    min_ruble = min(single, multi, combined)
    
    print(min_ruble)
    
if __name__ == '__main__':
    main()