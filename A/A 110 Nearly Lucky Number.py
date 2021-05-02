# https://codeforces.com/problemset/problem/110/A

n = input()

ln =  0
ln += n.count('4')
ln += n.count('7')

for i in range(len(str(ln))):
    if str(ln)[i] != '4' and str(ln)[i] != '7':
        print('NO')
        break
else:
    print('YES')