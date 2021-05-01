# https://codeforces.com/problemset/problem/4/B

d, t = map(int, input().split())
times = [list(map(int, input().split())) for _ in range(d)]

minT = [i[0] for i in times]
maxT = [i[1] for i in times]

if sum(minT) <= t and t <= sum(maxT):
    rest = t - sum(minT)
    i = 0
    while rest != 0 and i < d:
        if rest >= maxT[i] - minT[i]:
            rest -= maxT[i] - minT[i]
            minT[i] = maxT[i]
            i += 1
        else:
            minT[i] += rest
            rest = 0
    print('YES')
    print(' '.join([str(i) for i in minT]))
else:
    print('NO')