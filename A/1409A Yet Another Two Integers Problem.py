# https://codeforces.com/problemset/problem/1409/A

def main():
    t = int(input())
    cases = [[int(i) for i in input().split()] for i in range(t)]
    
    for case in cases:
        a, b = case[0], case[1]
        if (a-b) % 10 == 0:
            print(abs(a-b)//10)
        else:
            print(abs(a-b)//10 + 1)

if __name__ == '__main__':
    main()