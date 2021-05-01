# https://codeforces.com/problemset/problem/1/B

import re

n = int(input())
coordinates = [input() for _ in range(n)]

def strToNum(str):
    temp = [ord(char)-64 for char in str]
    n = 0
    t = 0
    for i in temp[::-1]:
        n += i * 26**t
        t += 1
    return n

def numToStr(num):
    temp = []
    while num > 0:
        if num%26 != 0:
            temp.append(num%26)
            num //= 26
        else:
            num = num //26 - 1
            temp.append(26)
    return ''.join([chr(i+64) for i in temp[::-1]])

for c in coordinates:
    if re.match('^R\d+C\d+$', c):
        s = c.find('C')
        row = c[1:s]
        col = int(c[s+1:])
        print(f"{numToStr(col)}{row}")
    else:
        s = None
        for idx, char in enumerate(c):
            if char.isdigit():
                s = idx
                break        
        col = c[:s]
        row = c[s:]
        print(f"R{row}C{strToNum(col)}")