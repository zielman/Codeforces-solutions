# https://codeforces.com/problemset/problem/1374/B

t = int(input())
nums = [int(input()) for i in range(t)]

for n in nums:
    a = 0
    b = 0
    while n % 2 == 0:
        n //= 2
        a += 1
    while n % 3 == 0:
        n //= 3
        b += 1
    if n == 1 and a <= b:
        print(2 * b - a )
    else:
        print(-1)