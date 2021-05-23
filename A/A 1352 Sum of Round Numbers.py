# https://codeforces.com/problemset/problem/1352/A

t = int(input())
cases = [input() for i in range(t)]

for n in cases:
    nor = [idx for idx, char in enumerate(n) if char != '0']
    k = []
    for idx in nor:
        k.append(f"{n[idx]}{'0' * (len(n) - 1 - idx)}")
    
    print(len(k))
    print(' '.join(k))