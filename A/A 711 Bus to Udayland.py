# https://codeforces.com/problemset/problem/711/A

t = int(input())
bus = [input() for _ in range(t)]

for idx, row in enumerate(bus):
    if row.find('OO') != -1:
        bus[idx] = bus[idx].replace('OO', '++', 1)
        print('YES')
        print(*bus, sep='\n')
        break    
else:
    print('NO')