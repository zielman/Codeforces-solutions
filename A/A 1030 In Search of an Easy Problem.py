# https://codeforces.com/problemset/problem/1030/A

n = int(input())
o = list(map(int, input().split()))

print('HARD' if o.count(1) != 0 else 'EASY')