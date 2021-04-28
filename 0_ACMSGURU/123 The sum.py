# https://codeforces.com/problemsets/acmsguru/problem/99999/123

def sumFib(n):
    if n <= 2:
        return n
    else:
        siv = [0]*(n)
        siv[0], siv[1] = 1, 1
        for i in range(2, n):
            siv[i] = siv[i-1] + siv[i-2]
        return sum(siv)

print(sumFib(int(input())))