# https://codeforces.com/problemset/problem/160/A

n = int(input())
coins = sorted(list(map(int, input().split())),reverse=True)

number_of_coins = 0
coins_value = 0

for coin in coins:
    number_of_coins += 1
    coins_value += coin
    if coins_value > sum(coins) / 2:
        break

print(number_of_coins)