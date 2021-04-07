# https://codeforces.com/problemset/problem/479/A

def main():
    a = int(input())
    b = int(input())
    c = int(input())

    t1 = a + b + c
    t2 = a + b * c
    t3 = (a + b) * c
    t4 = a * b + c
    t5 = a * (b + c)
    t6 = a * b * c

    print(max(t1, t2, t3, t4, t5, t6))

if __name__ == '__main__':
    main()