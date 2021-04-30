# https://codeforces.com/problemset/problem/231/A

inp = []

def get_input():
    inp.append(input())
    while len(inp) - 1 < int(inp[0]):
        get_input()

def main():
    
    get_input()
    inp.pop(0)
    
    solutions = 0
    
    for i in inp:
        a, b, c = map(int, i.split())
        if a + b + c >= 2:
            solutions += 1
    
    print(int(solutions))
    
if __name__ == '__main__':
    main()
    
