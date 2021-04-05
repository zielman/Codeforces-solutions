# https://codeforces.com/problemset/problem/110/A

def main():
    n = input()

    ln =  0
    ln += n.count('4')
    ln += n.count('7')

    for i in range(len(str(ln))):
        if str(ln)[i] == '4' or str(ln)[i] == '7':
            pass
        else:
            print('NO')
            break
    else:
        print('YES')

if __name__ == '__main__':
    main()