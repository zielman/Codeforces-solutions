# https://codeforces.com/problemset/problem/1296/B

t = int(input())
cases = [input() for _ in range(t)]

for case in cases:
    burles, spent = int(case), 0
    while burles > 9:
        spent += int(str(burles)[:-1]+'0') 
        r = int(str(burles)[-1])
        burles //= 10
        burles += r
    print(spent+burles)