# https://codeforces.com/problemset/problem/1331/C

def replace(string):
    temp = [string[0]]
    temp.append(string[5])
    temp.append(string[3])
    temp.append(string[2])
    temp.append(string[4])
    temp.append(string[1])
    temp = ''.join(temp)
    return temp

def main():
    
    inp = int(input())

    inp_bin = bin(inp)[2:].zfill(6)

    x = replace(str(inp_bin))

    print(int(x, 2))

if __name__ == '__main__':
    main()
