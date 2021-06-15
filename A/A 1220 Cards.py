# https://codeforces.com/problemset/problem/1220/A

n, s = int(input()), input()

ones = s.count('n')
zeros = (n-(ones*3))//4

print(f"{'1 '*ones}{'0 '*zeros}")