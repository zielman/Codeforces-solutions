# https://codeforces.com/problemset/problem/1358/A

def find_min_lamps(n: int, m: int) -> int:
    if n%2 ==0:
        count = n//2 * m
    else:
        if m%2 == 0:
            count = m//2 * n
        else:
            count = n//2 * m + m//2 + 1 
    return count

def main():
    t = int(input())
    cases = [list(map(int, input().split())) for _ in range(t)]
    for case in cases:
        print(find_min_lamps(case[0], case[1]))

if __name__=='__main__':
    main()