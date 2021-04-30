# https://codeforces.com/problemset/problem/467/A

def main():
    n = int(input())
    rooms = []
    for i in range(n):
        rooms.append(list(map(int, input().split())))

    ans = 0
    for room in rooms:
        if room[1] - room[0] >= 2:
            ans += 1
    
    print(ans)

if __name__ == '__main__':
    main()