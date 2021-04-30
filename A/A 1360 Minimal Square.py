# https://codeforces.com/problemset/problem/1360/A

def main():
    t = int(input())
    cases = [list(map(int, input().split())) for case in range(t)]

    for case in cases:
        a, b = case[0], case[1]
        r = (max(a,b) / min(a,b)) 

        if r <= 2:
           print((2*min(a,b))**2)
        else:
            print(max(a,b)**2)

if __name__ == '__main__':
    main()