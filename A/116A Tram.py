# https://codeforces.com/problemset/problem/116/A

def main():
    n = int(input())
    stops = []
    for i in range(n):
        stops.append(list(map(int, input().split())))

    p = 0
    peak_p = 0
    for stop in stops:
        p -= stop[0]
        p += stop[1]
        peak_p = max(p, peak_p)

    print(peak_p)
    
if __name__ == '__main__':
    main()