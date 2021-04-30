# https://codeforces.com/problemset/problem/791/A

def main():
    a, b = map(int, input().split()) # the weight of Limak and the weight of Bob respectively

    ans = 0
    while a <= b:
        a *= 3
        b *= 2
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()