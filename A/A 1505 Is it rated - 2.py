# https://codeforces.com/problemset/problem/1505/A
  
while True:
    try:
        if input() == 'Is it rated?':
            print('NO')
    except EOFError:
        break