# https://codeforces.com/problemset/problem/155/A

def main():
    n = int(input())
    p = [int(i) for i in input().split()]

    maxP, minP = p[0], p[0]
    a = 0
    for i in range(1, n):
        if p[i] > maxP:
            a += 1
            maxP = p[i]
        elif p[i] < minP:
            a += 1  
            minP = p[i]  
    print(a)

if __name__ == '__main__':
    main()