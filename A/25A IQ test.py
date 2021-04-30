# https://codeforces.com/problemset/problem/25/A

n = int(input())
nums = [int(i) for i in input().split()]

e, last_e = 0, 0
o, last_o = 0, 0

for n in nums:
    if n % 2 == 0:
        e += 1
        last_e = n
    elif n % 2 == 1:
        o += 1
        last_o = n
    
    if e > 1 and o == 1:
        print(nums.index(last_o) + 1)
        break
    elif o > 1 and e == 1:
        print(nums.index(last_e) + 1)
        break