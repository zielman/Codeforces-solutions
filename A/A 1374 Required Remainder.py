# https://codeforces.com/problemset/problem/1374/A

def main():
    t = int(input())
    cases = [[int(i) for i in input().split()] for i in range (t)]
    for case in cases:
        x, y, n = case[0], case[1], case[2]
        if n%x >= y:
            print(n - n%x + y)
        else:
            print(n - n%x + (y-x))
'''
# 2x slower but using almost 0 memory

def main():
    t = int(input())
    for i in range(t):
        x, y, n = map(int, input().split())
        
        if n%x >= y:
            print(n - n%x + y)
        else:
            print(n - n%x + (y-x))
'''            
if __name__ == '__main__':
    main()