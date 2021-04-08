# https://codeforces.com/problemset/problem/1367/A
    
def main():
    t = int(input())
    for i in range(t):
        s = input()
        ss = [s[0]]
        for i in range(0, len(s)-1, 2):
            ss.append((s[i], s[i+1])[1])
        print(''.join(ss))
    
if __name__ == '__main__':
    main()