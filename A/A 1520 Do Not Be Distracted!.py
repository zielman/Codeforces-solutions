# https://codeforces.com/problemset/problem/1520/B

t = int(input())
cases = [[int(input()), input()] for _ in range(t)]

for case in cases:
    tasks = []
    sus = 'YES'
    for i in range(case[0]):
        if case[1][i] in tasks:
            if case[1][i] == case[1][i-1]:
                sus = "YES"
            else:
                sus = 'NO'
                break
        else:
            tasks.append(case[1][i])
    print(sus)