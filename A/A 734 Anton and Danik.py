# https://codeforces.com/problemset/problem/734/A

def main():
    n = int(input())
    s = input()

    A = s.count('A')
    D = s.count('D')

    if A == D:
        print('Friendship')
    elif A > D:
        print('Anton')
    else:
        print('Danik')

if __name__ == '__main__':
    main()