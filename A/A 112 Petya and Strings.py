# https://codeforces.com/problemset/problem/112/A

def main():
    
    string_1 = input().lower()
    string_2 = input().lower()

    for i in range(0, len(string_1)):
        if string_1[i] == string_2[i]:
            continue
        if string_1[i] < string_2[i]:
            print(-1)
            break
        if string_1[i] > string_2[i]:
            print(1)
            break
    else:
        print(0)

if __name__ == '__main__':
    main()