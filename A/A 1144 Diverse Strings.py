# https://codeforces.com/problemset/problem/1144/A

def is_diverse(s: str) -> bool:
    arr = sorted(char for char in s)
    if (ord(arr[-1]) - ord(arr[0]) + 1 == len(s)) and (len(set(arr)) == len(s)):
        return True
    else:
        return False

def main():
    t = int(input())
    cases = [input() for _ in range(t)]
    for case in cases:
        print('Yes' if is_diverse(case) else 'No')

if __name__=='__main__':
    main()