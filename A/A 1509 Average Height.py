# https://codeforces.com/problemset/problem/1509/A

def main():
    t = int(input())
    cases = [[input(), list(map(int, input().split()))] for i in range(t)]

    for case in cases:
        ans = list(sorted(case[1], key=lambda x: [x % 2, x]))    
        print(' '.join([str(i) for i in ans]))

if __name__ == '__main__':
    main()