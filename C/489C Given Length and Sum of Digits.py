# https://codeforces.com/problemset/problem/489/C

def MaxToMin(string):
    min = string[::-1]
    for idx, char in enumerate(min):
            if char == '0':
                pass
            else:
                min = f"{min[:idx]}{int(min[idx])-1}{min[idx+1:]}"
                break
    return int(min) + int(f"1{str(0) * (len(string) - 1)}")

def main():

    m, s = map(int, input().split()) # m =  the length of the int, s =  the sum of the digits
    
    min = None
    max = None
    
    if s == 0 and m > 1 or m * 9 < s:
        min = -1
        max = -1
    elif s == 0 and m == 1:
        min = 0
        max = 0
    else:
        if s % 9 == 0:
            max = f"{str(9) * int(s / 9)}{str(0) * int(m - (s / 9))}"
            min = MaxToMin(max)
        else:
            max = f"{str(9) * int(s / 9)}{s % 9}{str(0) * int(m - (s / 9))}"
            min = MaxToMin(max)

    print(min, max)

if __name__ == '__main__':
    main()
