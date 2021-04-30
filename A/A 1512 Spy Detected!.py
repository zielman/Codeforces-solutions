# https://codeforces.com/problemset/problem/1512/A

def main():
    t = int(input())
    cases = [[int(input()), [int(i) for i in input().split()]] for i in range(t)]
    
    for case in cases:
        n, an = case[0], case[1]

        anSet = list(set(an))
        a, b = an.count(anSet[0]), an.count(anSet[1])
        if a < b:
            print(an.index(anSet[0])+1)
        else:
            print(an.index(anSet[1])+1)

if __name__ == '__main__':
    main()