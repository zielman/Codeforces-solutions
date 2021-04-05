# https://codeforces.com/problemset/problem/1505/C

def split(string):
    return [char for char in string]

def main():
    word = input()
    check =[]

    for l in split(word):
        check.append(ord(l) - 65)

    for i in range(len(check)-2):
        if (check[i] + check[i+1]) % 26 == check[i+2]:
            pass
        else:
            print('NO')
            break
    else:
        print('YES')

if __name__ == '__main__':
    main()