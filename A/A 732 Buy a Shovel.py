# https://codeforces.com/problemset/problem/732/A

k, r = input().split()

i = 1
t = int(k[-1])
while i <= 10:
    if int(str(t)[-1]) == int(r):
        print(i)
        break
    elif int(str(t)[-1]) == 0:
        print(i)
        break
    else:
        t += int(k[-1]) 
    i += 1