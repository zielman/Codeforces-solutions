# https://codeforces.com/problemset/problem/1541/A

t = int(input())
cases = [int(input()) for _ in range(t)]

for n in cases:
    test = [_+1 for _ in range(n)]
    
    for i in range(0, n-1, 2):
        test[i], test[i+1] = test[i+1], test[i]

    if n%2 != 0 and n > 2:
        test[-3], test[-2], test[-1] = test[-1], test[-2], test[-3]
        
    print(f"{' '.join([str(i) for i in test])}")