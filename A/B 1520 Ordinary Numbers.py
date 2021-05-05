# https://codeforces.com/problemset/problem/1520/B

t = int(input())
cases = [input() for _ in range(t)]

for num in cases:

    ans = 0

    if num >= num[0] * len(num):
        ans += int(num[0]) + (9*(len(num)-1)) 
    else:
        ans += int(num[0]) + (9*(len(num)-1))-1

    print(ans)   