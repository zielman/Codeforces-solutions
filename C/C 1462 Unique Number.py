# https://codeforces.com/problemset/problem/1462/C

t = int(input())
cases = [int(input()) for _ in range(t)]

for num in cases:
    if num > 45:
        print(-1)
    else:
        i, buff = 9, []
        while num > i:
            buff.append(i)
            num -= i
            i -= 1
        buff.append(num)
        print(''.join(str(i) for i in buff[::-1]))