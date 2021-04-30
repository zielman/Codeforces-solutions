# https://codeforces.com/problemset/problem/581/A

def main():
    a, b = map(int, input().split())
   
    x = max(a, b) - (max(a, b) - min(a, b))
    y = (max(a, b) - x) // 2

    print(x, y)

if __name__ == '__main__':
    main()