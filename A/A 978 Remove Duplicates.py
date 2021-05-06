# https://codeforces.com/problemset/problem/978/A

n = int(input())
arr = list(map(int, input().split()))

ans = []
for num in arr[::-1]:
    if num not in ans:
        ans.append(num)

print(len(ans))
print(' '.join(str(i) for i in ans[::-1]))