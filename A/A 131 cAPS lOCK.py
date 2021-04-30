# https://codeforces.com/problemset/problem/131/A

def isLower(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return True
    else:
        return False

def main():
    word = input()
    u = 0
    l = 0
    for c in word:
        if isLower(c):
            l += 1
        else:
            u += 1

    if u == len(word): # all upper
        print(word.lower()) 
    elif isLower(word[0]) and u + 1 == len(word): # first low & rest upper
        print(f"{word[0].upper()}{word[1:].lower()}")
    else:
        print(word)

if __name__ == '__main__':
    main()