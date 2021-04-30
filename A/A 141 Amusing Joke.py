# https://codeforces.com/problemset/problem/141/A

def main():
    gName = input()
    rHost = input()
    pile = input()
    
    d = {}
    for char in gName+rHost:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    
    dPile = {}
    for char in pile:
        if char not in dPile:
            dPile[char] = 1
        else:
            dPile[char] += 1

    for key in dPile:
        if key in d and dPile[key] == d[key] and len(dPile) == len(d):
            pass
        else:
            print('NO')
            break
    else:
        print('YES')

if __name__ == '__main__':
    main()