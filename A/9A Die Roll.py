# https://codeforces.com/problemset/problem/9/A

def main():
    y, w = map(int, input().split())

    numerator = 7 - max(y, w)

    if numerator == 6:
        print(f"{1}/{1}")
    elif numerator == 4:
        print(f"{2}/{3}")
    elif numerator == 3:
        print(f"{1}/{2}")
    elif numerator == 2:
        print(f"{1}/{3}")
    else:
        print(f"{numerator}/{6}")

if __name__ == '__main__':
    main()