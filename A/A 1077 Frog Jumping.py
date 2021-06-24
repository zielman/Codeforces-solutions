# https://codeforces.com/problemset/problem/1077/A

t = int(input())
frogs = [tuple(map(int, input().split())) for _ in range(t)]

for frog in frogs:
    a, b, k = map(int, frog)

    print(a*(k//2)-b*(k//2)) if k%2==0 else print((a*(k//2+1))-(b*(k//2)))