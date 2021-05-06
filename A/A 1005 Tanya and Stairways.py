# https://codeforces.com/problemset/problem/1005/A

n, arr = int(input()), list(map(int, input().split()))

stairways, steps = 0, [] 

if n >= 2:
    for i in range(n-1):
        if arr[i] >= arr[i+1]:
            stairways += 1
            steps.append(arr[i])

    if arr[-1] <= arr[-2]:
        stairways += 1
        steps.append(arr[-1])
    else:
        stairways += 1
        steps.append(arr[-1])

    print(stairways)
    print(' '.join(str(i) for i in steps))

else:
    print(1)
    print(1)