# https://codeforces.com/problemset/problem/703/A

def main():
    n = int(input())
    rounds = [list(map(int, input().split())) for _ in range(n)]

    m = 0
    c = 0
    for round in rounds:
        if round[0] > round[1]:
            m += 1
        elif round[0] < round[1]:
            c += 1

    if m > c:
        print('Mishka')
    elif m < c:
        print('Chris')
    else:
        print('Friendship is magic!^^')

if __name__ == '__main__':
    main()