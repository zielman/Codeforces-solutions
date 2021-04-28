# https://codeforces.com/problemset/problem/149/A

def main():
    k = int(input())
    months = sorted(list(map(int, input().split())), reverse=True)

    if k == 0:
        print(0)
    elif k > sum(months):
        print(-1)
    else:
        grow = 0
        for i in range(12):
            if months[i] + grow < k:
                grow += months[i]
            else:
                print(i+1)
                break

if __name__ == '__main__':
    main()