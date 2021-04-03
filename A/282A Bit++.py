# https://codeforces.com/problemset/problem/282/A

def main():
    
    statements = []

    def get_input():
        statements.append(input()) 
        while len(statements) - 1 < int(statements[0]):
            get_input()

    get_input()
    statements.pop(0)
    inp = 0
    for stat in statements:
        if 'X' in stat:
            if '+' in stat:
                inp += 1
            elif '-' in stat:
                inp -= 1
    print(inp)
    
if __name__ == '__main__':
    main()