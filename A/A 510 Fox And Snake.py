# https://codeforces.com/problemset/problem/510/A

n, m = map(int, input().split()) 

for i in range(1, n+1):
    if i % 2 != 0:
        print('#'*m)
    else:
        if i//2 % 2 != 0:
            print(f"{'.'*(m-1)}#")
        else:
            print(f"#{'.'*(m-1)}")