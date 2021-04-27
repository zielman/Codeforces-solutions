# https://codeforces.com/problemset/problem/1517/A

def get_largest_2050(x):
    if len(str(x)) <=4 or int(f"2050{'0' * (len(str(x)) - 4)}") <= x:
        return int(f"2050{'0' * (len(str(x)) - 4)}")
    else:
        return int(f"2050{'0' * (len(str(x)) - 5)}")

def main():
    t = int(input())
    cases = [int(input()) for _ in range(t)]

    for case in cases:
        if case % 2050 != 0:
            print('-1')
        else:
            a = case
            b = get_largest_2050(a)
            i = 0
            while a != 0:
                i += a//b
                a -= b * (a//b)
                b = get_largest_2050(a)

            print(i)
                
if __name__ == '__main__':
    main()