# https://codeforces.com/problemset/problem/69/A

coordinates = []

def get_input():
    coordinates.append(input()) 
    while len(coordinates) - 1 < int(coordinates[0]):
        get_input()

get_input()
coordinates.pop(0)

x = 0
y = 0
z = 0

for coord in coordinates:
    a, b, c = map(int, coord.split())
    x += a
    y += b
    z += c

if x == 0:
    if y == 0:
        if z == 0:
            print('YES')
else:
    print('NO')