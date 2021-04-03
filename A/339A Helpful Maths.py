# https://codeforces.com/problemset/problem/339/A

def split(string):
    return [char for char in string]

def main():
    
    inp = input()
    inp_split = split(inp)

    new_list = []

    for item in inp_split:
        try:
            if isinstance(int(item), int):
                new_list.append(int(item))
        except ValueError:
            pass

    new_list.sort()

    out = []

    for i in new_list:
        out.append(i)
        out.append('+')
    
    out.pop(-1)

    print(''.join([str(elem) for elem in out]))

if __name__ == '__main__':
    main()
