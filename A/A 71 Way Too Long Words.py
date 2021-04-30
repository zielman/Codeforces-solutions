#https://codeforces.com/problemset/problem/71/A

words = []

def get_input():
    words.append(input()) 
    while len(words) - 1 < int(words[0]):
        get_input()

def replace(str):
    return print(f"{str[0]}{len(str)-2}{str[-1]}")

def main():
    
    get_input()
    
    words.pop(0)

    for word in words:
        if len(word) > 10:
            replace(word)
        else:
            print(word)

if __name__ == '__main__':
    main()