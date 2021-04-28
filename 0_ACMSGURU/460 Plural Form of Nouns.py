# https://codeforces.com/problemsets/acmsguru/problem/99999/460

def SingularToPlural(s):
    if s[-2:] == 'ch' or s[-1] == 'x' or s[-1] == 's' or s[-1] == 'o':
        return f"{s}es"
    elif s[-2:] == 'fe':
        return f"{s[:-2]}ves"
    elif s[-1] == 'f':
        return f"{s[:-1]}ves"
    elif s[-1] == 'y':
        return f"{s[:-1]}ies"
    else:
        return f"{s}s"

n = int(input())
words = [input() for _ in range(n)]

for word in words:
    print(SingularToPlural(word))