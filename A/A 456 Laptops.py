# https://codeforces.com/problemset/problem/456/A

n = int(input())
laptops = [tuple(map(int, input().split())) for _ in range(n)]

laptops = sorted(laptops, key=lambda x: x[1], reverse=True)
laptops = sorted(laptops, key=lambda x: x[0])

for i in range(n-1):
    if laptops[i][0] < laptops[i+1][0] and laptops[i][1] > laptops[i+1][1]:
        print('Happy Alex')
        break
else:
    print('Poor Alex')