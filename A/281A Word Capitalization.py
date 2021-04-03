# https://codeforces.com/problemset/problem/281/A

def main():

    inp = input()

    def get_rest(string):
        if len(string) == 1:
            pass
        else:
            return inp[-(len(inp) - 1):]

    rest = get_rest(inp)
    
    if rest == None:
        print(f"{inp[0].upper()}")
    else:
        print(f"{inp[0].upper()}{rest}")
    
if __name__ == '__main__':
    main()