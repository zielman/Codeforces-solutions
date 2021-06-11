
# https://codeforces.com/problemset/problem/1538/A
    
t = int(input())
cases = [(int(input()), list(map(int, input().split()))) for _ in range(t)]
    
for case in cases:
    n, arr = case[0], case[1]

    l, g = arr.index(min(arr)), arr.index(max(arr))

    print(sum(sorted([(min(l,g)+1), (n-max(l,g)), (max(l,g)-min(l,g))])[:2]))