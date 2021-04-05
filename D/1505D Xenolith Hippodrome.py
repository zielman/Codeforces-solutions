# https://codeforces.com/problemset/problem/1505/D

def number_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def main():
    n, m = map(int, input().split())
    test = number_to_base(n, m)

    if len(test) == len(set(test)):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()