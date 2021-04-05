# https://codeforces.com/problemset/problem/1506/C

from difflib import SequenceMatcher

def main():
    t = int(input())
    cases = []
    for i in range(t):
        a = input()
        b = input()
        cases.append([a, b])

    for case in cases:
        match = SequenceMatcher(None, case[0], case[1]).find_longest_match(0, len(case[0]), 0, len(case[1]))
        if match[2] == 0:
            steps = len(case[0]) + len(case[1])
            print(steps)
        else:
            steps = len(case[0]) + len(case[1]) - 2 * match[2]
            print(steps)

if __name__ == '__main__':
    main()