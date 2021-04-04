# https://codeforces.com/problemset/problem/200/B

def average(lst):
    return sum(lst) / len(lst)

def main():
    n = int(input())
    np = list(map(int, input().split()))

    print(average(np))

if __name__ == '__main__':
    main()