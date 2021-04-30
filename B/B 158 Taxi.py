# https://codeforces.com/problemset/problem/158/B

n = int(input())
s = list(map(int, input().split()))

taxis = 0

fours = s.count(4)
threes = s.count(3)
twos = s.count(2)
ones = s.count(1) 

# 4
taxis += fours
fours = 0

# 3, 1
temp = min(threes, ones)
taxis += temp
threes -= temp
ones -= temp

# 2, 2
if twos % 2 == 0 and twos >= 2:
    taxis += int(twos / 2)
    twos = 0
elif twos % 2 == 1 and twos >= 3:
    taxis += int((twos - 1) / 2)
    twos = 1

# 2, 1, 1
if twos == 1 and ones >= 2:
    taxis += 1
    twos = 0
    ones -= 2

# 1, 1, 1, 1
if ones >= 4:
    taxis += int(ones / 4 - (ones % 4)/4)
    ones -= int(ones / 4 - (ones % 4)/4) * 4

# all perfect taxis included above

if ones == 1 and twos == 1:
    taxis += 1
    ones = 0
    twos = 0
elif ones >= 1 and ones <= 3 and twos == 0:
    taxis += 1
    ones = 0
else:
    taxis += twos
    taxis += threes

print(taxis)