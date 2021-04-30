# https://codeforces.com/problemset/problem/263/A

def main():
    
    matrix = []
    
    for i in range(5):
        inp = list(map(int, input().split()))
        matrix.append(inp)

    i_row = 0
    i_column = 0

    for row in matrix:
        i_row += 1
        if 1 in row:
            i_column = row.index(1) + 1
            break

    print(abs(3 - i_column) + abs(3 - i_row))

if __name__ == '__main__':
    main()
