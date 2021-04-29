# https://codeforces.com/problemsets/acmsguru/problem/99999/118
 
def digit_root(n): 
    return (n - 1) % 9 + 1
 
k = int(input())
 
for _ in range(k):
    case = list(map(int, input().split()))
    exp = 0
    t = 1
    for i in range(1, case[0]+1):
        t *= case[i]
        exp += t
    print(digit_root(exp))