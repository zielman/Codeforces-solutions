# https://codeforces.com/problemset/problem/118/A

vowels = {"A", "O", "Y", "E", "U", "I"}

def split(word):
    return [char for char in word]

def main():
    
    inp = input().lower()
    inp_split = split(inp)
    
    ans = []
    
    for i in inp_split:
        if i.upper() in vowels:
            continue
        else:
            ans.append(".")
            ans.append(i)
    
    print(''.join(ans)) 
    
if __name__ == '__main__':
    main()