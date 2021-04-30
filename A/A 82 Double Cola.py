# https://codeforces.com/problemset/problem/82/A

n = int(input())
q = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']

i = 1
while n > i*5:
    n -= i*5
    i *= 2

print(q[(n-1)//i])