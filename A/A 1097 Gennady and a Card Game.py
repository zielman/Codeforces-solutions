# https://codeforces.com/problemset/problem/1097/A

table, hand = input(), list(input().split())

for card in hand:
    if card[0] == table[0] or card[1] == table[1]:
        print('YES')
        break
else:
    print('NO')