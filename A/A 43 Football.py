# https://codeforces.com/problemset/problem/43/A

n = int(input())
goals = [input() for _ in range(n)]

score = {}

for goal in goals:
    if goal not in score:
        score[goal] = 1
    else:
        score[goal] += 1

print(max(score, key=lambda key: score[key]))