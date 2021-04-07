# https://codeforces.com/problemset/problem/61/A

def main():
    n1 = input()
    n2 = input()
    
    n = []
    i = 0
    while i < len(n1):
        if n1[i] == n2[i]:
            n.append('0')
            i += 1
        else:
            n.append('1')
            i += 1
    print(''.join(n))

if __name__ == '__main__':
    main()