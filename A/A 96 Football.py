# https://codeforces.com/problemset/problem/96/A

def is_dangerous(x: str) -> bool:
    d_counter = 0
    for p in range(1, len(x)):
        if int(x[p]) == int(x[int(p)-1]):
            d_counter += 1
            if d_counter == 6:
                return True
        else:
            d_counter = 0
    else:
        return False

print('YES' if is_dangerous(input()) else 'NO')