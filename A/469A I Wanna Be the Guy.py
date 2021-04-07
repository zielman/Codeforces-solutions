# https://codeforces.com/problemset/problem/469/A

def main():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    
    if x[0]== n or y[0] == n:
        print('I become the guy.')
    else:
        if n == len(set(x[1:x[0]+1] + y[1:y[0]+1])):
            print('I become the guy.')
        else:
            print('Oh, my keyboard!')

if __name__ == '__main__':
    main()