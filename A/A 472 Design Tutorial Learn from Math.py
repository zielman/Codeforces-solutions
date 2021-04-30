# https://codeforces.com/problemset/problem/472/A

def main():
    num = int(input())

    if num % 4 == 0:
        print(num // 2, num // 2)
    elif (num - 9) % 2 == 0:
        print(9, num - 9)
    else:
        print(4, num - 4)

if __name__ == '__main__':
    main()