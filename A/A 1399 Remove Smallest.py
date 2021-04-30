# https://codeforces.com/problemset/problem/1399/A

def main():
    t = int(input())
    tCases = [[int(input()), list(map(int, input().split()))] for i in range(t)]
    
    for case in tCases:
        aList = list(set(case[1]))
        aList.sort()

        if len(aList) == 1:
            print('YES')
        else:
            for i in range(len(aList) - 1):
                if aList[i+1] - aList[i] != 1:
                    print('NO')
                    break
            else:
                print('YES')

if __name__ == '__main__':
    main()