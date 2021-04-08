# https://codeforces.com/problemset/problem/785/A

def main():
    n = int(input())
    fav = {'T': 4, 'C': 6, 'O': 8, 'D': 12, 'I': 20}
    c = 0
    for i in range(n):
        c += fav[input()[0]]
    print(c)

if __name__ == '__main__':
    main()