# https://codeforces.com/problemset/problem/160/A

def get_input():
    number_of_coins = int(input())
    coins = (input().split())
    for c in range(0, len(coins)):
        coins[c] = int(coins[c])
    return number_of_coins, coins
        
def main():

    inp = get_input()
    
    number_of_coins = inp[0]
    coins = inp[1]
    
    total_coins = sum(coins)
    
    coins.sort(reverse=True)
    
    min_c = 0
    c_value = 0
  
    for coin in coins:
        min_c += 1
        c_value += coin
        if c_value <= (total_coins / 2):
            pass
        else:
            break
    
    print(min_c)
            
if __name__ == '__main__':
    main()