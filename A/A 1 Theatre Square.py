# https://codeforces.com/problemset/problem/1/A

import math
    
n, m, a = map(int, input().split())
print(math.ceil(n / a) * math.ceil(m / a))